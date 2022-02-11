# coding = utf-8
# Author: Shenbq
# Date: 2022/1/22 11:45
import os

import yaml


# 读取接口信息
def read_yaml(key):
    with open(os.getcwd() + '/api_config.yaml', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[key]


# 读取鉴权码yaml文件
def read_token_yaml(key):
    with open(os.getcwd() + '/configs/access_token', encoding='utf-8') as f:
        token = yaml.load(stream=f, Loader=yaml.FullLoader)
        return token[key]


# 写入鉴权码
def write_token(data):
    with open(os.getcwd() + '/configs/access_token', mode='w', encoding='utf-8') as f:
        yaml.dump(data, stream=f, allow_unicode=True)

# # 清空鉴权码yaml文件
# def clear_token():
#     with open(os.getcwd() + '/configs/access_token', mode='w', encoding='utf-8') as f:

# 读取用户接口信息
def read_test_yaml():
    with open(os.getcwd() + '/create_token.yaml', encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value