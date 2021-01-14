# !/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time  : 2021/1/13 下午7:49
# @Author: 张伟
# @EMAIL: Jtyoui@qq.com
# @Notes : restFul接口
from fastapi import FastAPI, Query

from service import *

app = FastAPI(title='回答系统接口', description='专业植物病理回答系统', version='1.0')


@app.get('/wss/qa', summary='回答接口', response_model=ResponseModal)
def qa(question: str = Query(..., description='一句问话')):
    try:
        data = answer(question)
        if data:
            similar = similarity(question)
            return ResponseModal(code=200, data=data, sentence=similar)
        else:
            rec = recommend(question)
            return ResponseModal(code=201, sentence=rec)
    except Exception as e:
        return ResponseModal(code=400, msg=str(e))


@app.get('/wss/hot', summary='热点问题', response_model=ResponseModal)
def hot(num: int = Query(..., description='数量')):
    h = get_hot(num)
    return ResponseModal(sentence=h)
