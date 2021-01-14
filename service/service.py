# !/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time  : 2021/1/14 下午6:40
# @Author: 张伟
# @EMAIL: Jtyoui@qq.com
# @Notes : 一些基本的服务
from pydantic import BaseModel

from config import QUE_INDEX, QUE_DOC
from operateES import find_key


class ResponseModal(BaseModel):
    """返回格式类型"""
    msg: str = 'success'
    code: int = 200
    data: str = ''
    sentence: list = []


def similarity(sentence: str) -> list:
    result = find_key(QUE_INDEX, QUE_DOC, sentence)
    return result


def recommend() -> list:
    return ['玉米大斑病什么病原？', '玉米大斑病病原', '玉米大斑病的病原属于什么性质']


def answer(sentence: str) -> str:
    return '玉米大斑病'


def get_hot(num: int) -> list:
    return ['玉米大斑病什么病原？', '玉米大斑病病原', '玉米大斑病的病原属于什么性质']
