# -*- coding:utf-8 -*-
# @author mark
# @since 2022/03/16 22:34:40
# @modified 2022/03/16 22:56:58
# @filename leveldb_bench.py


import leveldb
import os
import sys
import time

# print(os.path.abspath("."))
sys.path.append("./src")
# print(sys.path)

from utils.db_utils import rand_str, mem_deco, prepare_kv_data

def init_db():
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    return leveldb.LevelDB("tmp/leveldb")

@mem_deco("Test insert")
def test_insert(times, key_len = 20, value_len = 1024):
    db = init_db()

    data = prepare_kv_data(times, key_len, value_len)

    start_time = time.time()

    for key, value in data:
        db.Put(key.encode("utf-8"), value.encode("utf-8"))

    cost_time = time.time() - start_time
    qps = times / cost_time
    print("Test insert (%d) times, cost (%.2f)ms, qps (%.2f)" % (times, cost_time*1000, qps))
    


@mem_deco("Test query")
def test_query(times, key_len = 20):
    db = init_db()
    data = prepare_kv_data(times, 20, 1)

    start_time = time.time()
    for key, _ in data:
        key = rand_str(key_len)
        try:
            value = db.Get(key.encode("utf-8"))
        except KeyError:
            value = None

    cost_time = time.time() - start_time
    qps = times / cost_time
    print("Test query (%d) times, cost (%.2f)ms, qps (%.2f)" % (times, cost_time*1000, qps))
    

test_insert(100)
test_insert(1000)
test_insert(10000)

test_query(100)
test_query(1000)
test_query(10000)

