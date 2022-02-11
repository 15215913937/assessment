# coding = utf-8
# Author: Shenbq
# Date: 2022/1/26 16:27
import json

import requests


# 封装意味着这个方法能适应所有请求

class RequestUtil:
    sess = requests.session()

    def send_request(self, method, url, datas=None, **kwargs):
        # 获取请求方式，将获取到的请求方式先转换成字符串格式，再转换成小写格式
        method = str(method).lower()
        res = None
        if method == 'get':
            res = RequestUtil.sess.request(method=method, url=url, params=datas, **kwargs)
        elif method == 'post':
            # 把字典格式的数据转换成json字符串
            str_datas = json.dumps(datas)
            res = RequestUtil.sess.request(method=method, url=url, data=str_datas, **kwargs)
        else:
            pass
        return res
