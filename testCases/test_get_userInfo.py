# coding = utf-8
# Author: Shenbq
# Date: 2022/1/22 18:16
import requests

from common.request_util import RequestUtil
from readYaml import read_token_yaml, read_yaml


class TestGetUserInfo:
    def test_userinfo(self):
        header = {
            "Accept": read_yaml('header')['Accept'],
            "x-token": read_token_yaml('access_token')
        }
        url = read_yaml('host') + read_yaml('user')['url']
        res = RequestUtil().send_request(method='get', url=url,headers=header)
        # res = requests.get(url=url, headers=header)

        print(res.json())
