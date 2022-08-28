# -*- coding:utf-8 -*-
# @author mark
# @since 2022/03/16 21:45:12
# @modified 2022/03/16 22:55:58
# @filename sqlite_bench.py
import sqlite3
import os
import sys
import time
import shutil

# print(os.path.abspath("."))
sys.path.append("./src")
# print(sys.path)

from utils.db_utils import ResultPrinter, mem_deco, prepare_kv_data

printer = ResultPrinter()

class Database:

    def init(self):
        db = sqlite3.connect("tmp/test.db")
        sql = "CREATE TABLE IF NOT EXISTS `kv_store` (`key` text primary key, value text);"
        self.db = db
        self.execute(sql)

    def execute(self, sql, *args):
        cursorobj = self.db.cursor()
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
            self.db.commit()
            return kv_result
        except Exception:
            raise
    
    def close(self):
        self.db.close()

def init_db():
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    if os.path.exists("tmp/test.db"):
        os.remove("tmp/test.db")
        
    db = Database()
    db.init()
    return db


def test_insert(times, key_len = 20, value_len = 1024):
    db = init_db()

    data = prepare_kv_data(times, key_len, value_len)

    printer.trace_start()
    start_time = time.time()

    for key, value in data:
        sql = "INSERT INTO kv_store(`key`, `value`) VALUES (?, ?);"
        db.execute(sql, key, value)

    cost_time = time.time() - start_time

    printer.trace_end()
    printer.print_result("Insert", times, cost_time)

    # print("Test insert (%d) times, cost (%.2f)ms, qps (%.2f)" % (times, cost_time*1000, qps))
    
    db.close()



def test_batch_insert(times, key_len = 20, value_len = 1024):
    db = init_db()

    data = prepare_kv_data(times, key_len, value_len)

    printer.trace_start()
    start_time = time.time()

    for key, value in data:
        sql = "INSERT INTO kv_store(`key`, `value`) VALUES (?, ?);"
        db.execute(sql, key, value)

    cost_time = time.time() - start_time

    printer.trace_end()
    printer.print_result("Insert", times, cost_time)

    # print("Test insert (%d) times, cost (%.2f)ms, qps (%.2f)" % (times, cost_time*1000, qps))
    
    db.close()


def test_query(times, key_len = 20):
    db = init_db()

    data = prepare_kv_data(times, key_len, 1)
    printer.trace_start()

    start_time = time.time()
    for key, _ in data:
        sql = "SELECT * FROM kv_store WHERE key = ?;"
        db.execute(sql, key)

    cost_time = time.time() - start_time
    # qps = times / cost_time
    # print("Test query (%d) times, cost (%.2f)ms, qps (%.2f)" % (times, cost_time*1000, qps))
    
    printer.trace_end()
    printer.print_result("Query", times, cost_time)

    db.close()

printer.print_head()

test_insert(100)
test_insert(1000)
test_insert(10000)

test_query(100)
test_query(1000)
test_query(10000)