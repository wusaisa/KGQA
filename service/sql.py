# !/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time  : 2021/1/14 下午8:13
# @Author: 张伟
# @EMAIL: Jtyoui@qq.com
# @Notes : 建立数据库和表
import pymysql

from config import *


class MySQL:
    def __init__(self, info, host, user, passwd, charset):
        self.db_info = info
        self.conn = pymysql.connect(host=host, user=user, password=passwd, charset=charset)
        self.cursor = self.conn.cursor()

    @staticmethod
    def abs_null(tb_info, num):
        if tb_info['columns'][num][2] == 0:
            return ''
        else:
            return 'NOT NULL'

    def create_database(self):
        """创建库"""
        self.cursor.execute('show databases;')
        tables_tup = self.cursor.fetchall()
        for db_info in self.db_info:
            print(f"开始创建{db_info['db_name']}......")
            if f"('{db_info['db_name']}',)" in str(tables_tup):
                print(f'{db_info["db_name"]}已经存在,开始检查表结构......')
            else:
                try:
                    self.cursor.execute(f'CREATE DATABASE {db_info["db_name"]} character set utf8mb4;')
                except Exception as e:
                    print(f'error:{e}')
                    self.conn.rollback()
            self.create_table(db_info)
            print(f'{db_info["db_name"]}创建完毕!')
        self.close_mysql()

    def create_table(self, db_info):
        """创建表"""
        self.cursor.execute(f'use {db_info["db_name"]};')
        self.cursor.execute('SHOW tables;')
        table_list_info = self.cursor.fetchall()
        for tb_info in db_info['tb_info']:
            if f"('{tb_info['tb_name']}',)" in str(table_list_info):
                print(f'表{tb_info["tb_name"]}已经存在,开始添加字段......')
            else:
                my_table = f'CREATE TABLE {tb_info["tb_name"]}(' \
                           f'id INT NOT NULL AUTO_INCREMENT,' \
                           f'PRIMARY KEY (id)' \
                           f')CHARSET="utf8mb4"'
                try:
                    self.cursor.execute(my_table)
                except Exception as e:
                    print(f'error:{e}')
                    self.conn.rollback()
            self.add_column(db_info, tb_info)

    def add_column(self, db_info, tb_info):
        self.cursor.execute(f'SHOW COLUMNS FROM {tb_info["tb_name"]};')
        column_list = self.cursor.fetchall()
        for i in range(len(tb_info['columns'])):
            if f"('{tb_info['columns'][i][0]}'" in str(column_list):
                print(f'字段{tb_info["columns"][i][0]}已经存在!尝试创建其他字段......')
            else:
                ad_col = f'ALTER TABLE {tb_info["tb_name"]} ADD ' \
                         f'{tb_info["columns"][i][0]} ' \
                         f'{tb_info["columns"][i][1]} ' \
                         f'{self.abs_null(tb_info, i)}'
                try:
                    self.cursor.execute(ad_col)
                except Exception as e:
                    print(f'error:{e}')
                    self.conn.rollback()
        print(f'数据库{db_info["db_name"]}中表{tb_info["tb_name"]}创建完毕!')

    def close_mysql(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    # def add_hot(self, question: str):
    #     count = self.cursor.execute(f'SELECT COUNT(*) FROM hot WHERE question="{question}"')
    #     if count > 0:
    #         pass
    #     else:
    #         self.cursor.execute(f'INSERT INTO hot(question,num)')


if __name__ == '__main__':
    MySQL(DATABASES_INFO, HOST, USER, PASSWORD, CHARSET).create_database()  # 创建库
