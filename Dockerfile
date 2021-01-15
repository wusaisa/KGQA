FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-alpine3.10

MAINTAINER Jytoui <jtyoui@qq.com>

COPY ./requirements.txt /requirements.txt

# 加入pip源
ENV pypi https://pypi.douban.com/simple

# 安装Python3环境
RUN pip3 install --no-cache-dir -r /requirements.txt -i ${pypi}
COPY ./service /app