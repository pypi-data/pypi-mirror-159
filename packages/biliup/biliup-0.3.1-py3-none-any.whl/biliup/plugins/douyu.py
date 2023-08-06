import json
import requests
from urllib.parse import urlencode

from ykdl.extractors.douyu.util import ub98484234
from ykdl.util.http import get_content, get_response
from ykdl.util.match import match1

from biliup.config import config
from ..engine.decorators import Plugin
from ..plugins import logger
from ..engine.download import DownloadBase


@Plugin.download(regexp=r'(?:https?://)?(?:(?:www|m)\.)?douyu\.com')
class Douyu(DownloadBase):
    def __init__(self, fname, url, suffix='flv'):
        super().__init__(fname, url, suffix)
        self.vid = ''
        self.logger = logger

    def check_stream(self):
        logger.debug(self.fname)
        if len(self.url.split("douyu.com/")) < 2:
            logger.debug("直播间地址:" + self.url + " 错误")
            return False
        html = get_content(self.url)
        self.vid = match1(html, '\$ROOM\.room_id\s*=\s*(\d+)',
                     'room_id\s*=\s*(\d+)',
                     '"room_id.?":(\d+)',
                     'data-onlineid=(\d+)')
        roominfo = requests.get(f"https://www.douyu.com/betard/{self.vid}").json()['room']
        videoloop = roominfo['videoLoop']
        show_status = roominfo['show_status']
        if show_status != 1 or videoloop != 0:
            logger.debug("直播间" + self.vid + "：未开播或正在放录播")
            return False
        douyucdn = config.get('douyucdn') if config.get('douyucdn') else 'tct-h5'
        html_h5enc = requests.get(f'https://www.douyu.com/swf_api/homeH5Enc?rids={self.vid}').json()
        js_enc = html_h5enc['data']['room' + self.vid]
        params = {
            'cdn': douyucdn,
            'iar': 0,
            'ive': 0
        }
        ub98484234(js_enc, self, params)
        params['rate'] = 0
        data = urlencode(params).encode('utf-8')
        html_content = get_response(f'https://www.douyu.com/lapi/live/getH5Play/{self.vid}', data=data).json()
        live_data = html_content["data"]
        if type(live_data) is dict:
            self.raw_stream_url = f"{live_data.get('rtmp_url')}/{live_data.get('rtmp_live')}"
            self.room_title = roominfo['room_name']
            return True
