# coding = utf-8
# Author: Shenbq
# Date: 2022/1/22 15:19
import requests


def a():
    url = 'http://assessment.dctest.jcfor.com/api/admin/medical/login'
    json = {
        "loginName": "1",
        "password": "1"
    }
    header = {
        "Content-type": "application/json"
    }
    res = requests.post(url=url, json=json, headers=header)
    print(res.text)
if __name__ == '__main__':
    a()