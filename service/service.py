# !/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time  : 2021/1/14 下午6:40
# @Author: 张伟
# @EMAIL: Jtyoui@qq.com
# @Notes : 一些基本的服务
import json

from pydantic import BaseModel

from config import *
from operateES import find_key
from sql import MySQL


class ResponseModal(BaseModel):
    """返回格式类型"""
    msg: str = 'success'
    code: int = 200
    data: str = ''
    sentence: list = []


def similarity(sentence: str, num=5) -> list:
    """返回相似语句
    :param sentence: 问句
    :param num: 返回相似句前几条
    """
    result = find_key(QUE_INDEX, QUE_DOC, sentence, num)
    return result


def recommend(sentence: str, num=5) -> list:
    """返回推荐问题
    :param sentence: 问句
    :param num: 返回推荐问前几条
    """
    return ['玉米大斑病什么病原？', '玉米大斑病病原', '玉米大斑病的病原属于什么性质']


def answer(sentence: str) -> str:
    """搜索问句的答案"""
    return '玉米大斑病'


def get_hot(num: int) -> list:
    """获取热点问题
    :param num: 返回热点问题前几条
    """
    with MySQL(HOST, USER, PASSWORD, CHARSET, db=DB) as ms:
        result = ms.get_hot_num(num)
    return result


def insert_hot(question: str):
    """插入热点问题"""
    with MySQL(HOST, USER, PASSWORD, CHARSET, db=DB) as ms:
        ms.add_hot(question)


def insert_answer(question: str, data: str, sentence: list):
    """插入问答返回数据"""
    st = json.dumps(sentence, ensure_ascii=False)
    with MySQL(HOST, USER, PASSWORD, CHARSET, db=DB) as ms:
        ms.add_answer(question, data, st)
