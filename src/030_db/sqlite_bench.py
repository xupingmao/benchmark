# -*- coding:utf-8 -*-
# @author mark
# @since 2022/03/16 21:45:12
# @modified 2022/03/16 22:36:29
# @filename sqlite_bench.py
import sqlite3
import os
import sys
import time

# print(os.path.abspath("."))
sys.path.append("./src")
# print(sys.path)

from utils.db_utils import rand_str, mem_deco

def db_execute(db, sql, *args):
    cursorobj = db.cursor()
    try:
        cursorobj.execute(sql, args)
        kv_result = []
        result = cursorobj.fetchall()
        for single in result:
            resultMap = {}
            for i, desc in enumerate(cursorobj.description):
                name = desc[0]
                resultMap[name] = single[i]
            kv_result.append(resultMap)
        db.commit()
        return kv_result
    except Exception:
        raise

def init_db():
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    db = sqlite3.connect("tmp/test.db")
    sql = "CREATE TABLE IF NOT EXISTS `kv_store` (`key` text primary key, value text);"
    db_execute(db, sql)
    return db


@mem_deco("Test insert")
def test_insert(times, key_len = 20, value_len = 1024):
    db = init_db()
    start_time = time.time()

    for i in range(times):
        key = rand_str(key_len)
        value = rand_str(value_len)
        sql = "INSERT INTO kv_store(`key`, `value`) VALUES (?, ?);"
        db_execute(db, sql, key, value)

    cost_time = time.time() - start_time
    print("Test insert (%d) times, cost (%.2f)ms" % (times, cost_time*1000))
    
    db.close()


@mem_deco("Test query")
def test_query(times, key_len = 20):
    db = init_db()
    start_time = time.time()

    for i in range(times):
        key = rand_str(key_len)
        sql = "SELECT * FROM kv_store WHERE key = ?;"
        db_execute(db, sql, key)

    cost_time = time.time() - start_time
    print("Test query (%d) times, cost (%.2f)ms" % (times, cost_time*1000))
    
    db.close()

test_insert(100)
test_insert(1000)
test_insert(10000)

test_query(100)
test_query(1000)
test_query(10000)