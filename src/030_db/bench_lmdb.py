import lmdb
import os
import sys
import time

# print(os.path.abspath("."))
sys.path.append("./src")
# print(sys.path)

from utils.db_utils import ResultPrinter, prepare_kv_data

printer = ResultPrinter()

class Database:

    def init(self):
        self.env = lmdb.open("./tmp/lmdb", map_size=1024**3)

    def get(self, key):
        """通过key读取Value
        @param {bytes} key
        @return {bytes|None} value
        """
        with self.env.begin() as tx:
            value = tx.get(key.encode("utf-8"))
            if value != None:
                return value.decode("utf-8")
            return None

    def put(self, key, value, sync=False):
        """写入Key-Value键值对
        @param {bytes} key
        @param {bytes} value
        """
        with self.env.begin(write=True) as tx:
            tx.put(key.encode("utf-8"), value.encode("utf-8"))

    def close(self):
        self.env.close()

def init_db():
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    db = Database()
    db.init()
    return db


def test_insert(times, key_len = 20, value_len = 1024):
    db = init_db()

    data = prepare_kv_data(times, key_len, value_len)

    printer.trace_start()
    start_time = time.time()

    for key, value in data:
        db.put(key, value)

    cost_time = time.time() - start_time

    printer.trace_end()
    printer.print_result("Put", times, cost_time)

    # print("Test insert (%d) times, cost (%.2f)ms, qps (%.2f)" % (times, cost_time*1000, qps))
    
    db.close()


def test_query(times, key_len = 20):
    db = init_db()

    data = prepare_kv_data(times, key_len, 1)
    printer.trace_start()

    start_time = time.time()
    for key, _ in data:
        value = db.get(key)

    cost_time = time.time() - start_time
    # qps = times / cost_time
    # print("Test query (%d) times, cost (%.2f)ms, qps (%.2f)" % (times, cost_time*1000, qps))
    
    printer.trace_end()
    printer.print_result("Get", times, cost_time)

    db.close()

printer.print_head()

test_insert(100)
test_insert(1000)
test_insert(10000)

test_query(100)
test_query(1000)
test_query(10000)