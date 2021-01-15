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
    {"host": 'es01', "port": 9200},
    {"host": 'es02', "port": 9201},
    {"host": 'es03', "port": 9202}
]

QUE_INDEX = 'que_index'
QUE_DOC = 'que_doc'

DATABASES_INFO = [
    {
        'db_name': 'wss',
        'tb_info': [
            {
                'tb_name': 'hot',
                'columns': [
                    ('question', 'varchar(20)', 1),
                    ('id', 'int', 1),
                    ('num', 'int', 0)
                ]
            },
            {
                'tb_name': 'answer',
                'columns': [
                    ('question', 'varchar(255)', None),
                    ('id', 'int', 0),
                    ('data', 'varchar(255)', None),
                    ('sentence', 'text', None)
                ]
            }
        ]
    }
]

HOST = 'mysql'
USER = 'root'
PASSWORD = 'password'
CHARSET = 'utf8mb4'
DB = DATABASES_INFO[0]['db_name']
