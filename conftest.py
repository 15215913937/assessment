# coding = utf-8
# Author: Shenbq
# Date: 2022/1/23 10:42
import pytest


@pytest.fixture(scope='session', autouse=True)
def clear_data():
    print("开始测试啦！")
    yield
    print("结束测试啦!")
