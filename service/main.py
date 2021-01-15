# !/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time  : 2021/1/13 下午7:49
# @Author: 张伟
# @EMAIL: Jtyoui@qq.com
# @Notes : restFul接口
from fastapi import FastAPI, Query

from operateES import delete_index, create_index, batch_data
from service import *

app = FastAPI(title='回答系统接口', description='专业植物病理回答系统', version='1.0')


@app.get('/wss/createMysql', summary='初始化MYSQL数据库和表结构')
def create_mysql():
    with MySQL(HOST, USER, PASSWORD, CHARSET) as ms:
        ms.create_database(DATABASES_INFO)  # 创建数据库
    return {'code': 200, 'msg': '创建数据库成功'}


@app.get('/wss/createES', summary='初始化ElasticSearch数据')
def create_es():
    delete_index(QUE_INDEX, True)  # 删除索引
    create_index(QUE_INDEX, QUE_DOC)  # 创建索引
    batch_data(QUE_INDEX, QUE_DOC, 10000)  # 批量插入
    return {'code': 200, 'msg': '创建ElasticSearch数据成功'}


@app.get('/wss/qa', summary='回答接口', response_model=ResponseModal)
def qa(
        question: str = Query(..., description='一句问话', min_length=2),
        num: int = Query(5, description='返回推荐问或者相似问条数')):
    try:
        data = answer(question)
        insert_hot(question)
        if data:
            sentence = similarity(question, num)
            code = 200
        else:
            sentence = recommend(question, num)
            code = 201
        insert_answer(question, data, sentence)
        return ResponseModal(code=code, sentence=sentence, data=data)
    except Exception as e:
        return ResponseModal(code=400, msg=str(e))


@app.get('/wss/hot', summary='热点问题', response_model=ResponseModal)
def hot(num: int = Query(..., description='数量')):
    try:
        h = get_hot(num)
        return ResponseModal(sentence=h)
    except Exception as e:
        return ResponseModal(code=400, msg=str(e))
