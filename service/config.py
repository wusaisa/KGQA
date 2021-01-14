# !/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time  : 2021/1/14 上午9:55
# @Author: 张伟
# @EMAIL: Jtyoui@qq.com
# @Notes : 配置文件
import os

CUR_DIR = os.path.dirname(__file__)  # 当前文件夹路径
DATA_DIR = os.path.join(os.path.dirname(CUR_DIR), 'data')  # 数据文件夹路径
QUE_TXT = os.path.join(DATA_DIR, 'questions.txt')

HOST_LIST = [
    {"host": "127.0.0.1", "port": 9200},
    {"host": "127.0.0.1", "port": 9201},
    {"host": "127.0.0.1", "port": 9202}
]
