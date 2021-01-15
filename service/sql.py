# !/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time  : 2021/1/14 下午8:13
# @Author: 张伟
# @EMAIL: Jtyoui@qq.com
# @Notes : 建立数据库和表
import pymysql


class MySQL:
    def __init__(self, host, user, passwd, charset, db=None):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.charset = charset
        self.db = db

    @staticmethod
    def abs_null(tb_info, num):
        return '' if tb_info['columns'][num][2] == 0 else 'NOT NULL'

    def create_database(self, db_infos):
        """创建库"""
        self.cursor.execute('show databases;')
        tables_tup = self.cursor.fetchall()
        for db_info in db_infos:
            print(f"开始创建{db_info['db_name']}......")
            if f"('{db_info['db_name']}',)" in str(tables_tup):
                print(f'{db_info["db_name"]}已经存在,开始检查表结构......')
            else:
                self.cursor.execute(
                    f'CREATE DATABASE {db_info["db_name"]} character set utf8mb4;')
            self.create_table(db_info)
            print(f'{db_info["db_name"]}创建完毕!')

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
                self.cursor.execute(my_table)
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
                self.cursor.execute(ad_col)
        print(f'数据库{db_info["db_name"]}中表{tb_info["tb_name"]}创建完毕!')

    def __enter__(self):
        if self.db is None:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, charset=self.charset)
        else:
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.passwd, charset=self.charset,
                                        db=self.db)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is not None:
            self.conn.rollback()
            print('执行sql语句失败，发生了异常', exc_val)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def add_answer(self, question: str, data: str, sentence: str):
        """插入answer数据"""
        sql = F"INSERT INTO answer(question,data,sentence) value ('{question}','{data}','{sentence}')"
        self.cursor.execute(sql)
        return True

    def add_hot(self, question: str):
        """插入数据库用户咨询的问题"""
        self.cursor.execute(f'SELECT COUNT(*) FROM hot WHERE question="{question}"')
        count = self.cursor.fetchone()[0]
        if count:
            self.cursor.execute(f"UPDATE hot SET num=num+1 WHERE question='{question}'")
        else:
            self.cursor.execute(f"INSERT INTO hot(question,num) value ('{question}',1)")
        return True

    def get_hot_num(self, num: int):
        """获取num条热点问题"""
        sql = F"SELECT question FROM hot ORDER BY num DESC LIMIT {num}"
        result = self.cursor.execute(sql)
        if result > 0:
            ls = [i[0] for i in self.cursor.fetchall()]
        else:
            ls = []
        return ls
