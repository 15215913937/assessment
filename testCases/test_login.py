# coding = utf-8
# Author: Shenbq
# Date: 2022/1/22 11:01
import pytest
import requests
from ddt import ddt, data, unpack

from common.request_util import RequestUtil
from readYaml import read_yaml, write_token, read_test_yaml


class TestLogin:
    def setup(self):
        pass

    def teardown(self):
        pass
    @pytest.mark.parametrize("args_name",read_test_yaml())
    def test_correctLogin(self,args_name):
        # print(args_name)
        url = args_name['request']['url']
        json = args_name['request']['json']
        header = args_name['request']['header']
        res = RequestUtil().send_request(method='post', url=url, datas=json,headers = header)
        # res = requests.post(url=url, json=json, headers=header)
        print(res.json())

        if "token" in res.text:
            token = res.json()['data']['token']
            write_token({"access_token": token})
        # assert res.json()['data']['doctor']['name'] == '张三1'
    # def test_wrongLogin(self):
    #     return "b"
