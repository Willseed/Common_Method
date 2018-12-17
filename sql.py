# -*- coding: utf-8 -*-
import pymysql


def select_SQL(host, usename, password, database, sql):
    db = pymysql.connect(host, usename, password, database, charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return ''


def other_SQL(host, usename, password, database, sql):
    db = pymysql.connect(host, usename, password, database, charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
