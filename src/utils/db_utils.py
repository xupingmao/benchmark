# -*- coding:utf-8 -*-
# @author mark
# @since 2022/03/16 21:51:14
# @modified 2022/03/16 22:33:56
# @filename db_utils.py

import os
import time
import random
import psutil

def timeit(func, *args):
    t1 = time.time()
    ret = func(*args)
    cost_time = (time.time() - t1) * 1000
    print("cost time: %sms" % cost_time)

def rand_str(length):
    v = ""
    a = ord('A')
    b = ord('Z')
    for i in range(length):
        v += chr(random.randint(a, b))
    return v

def format_size(size):
    """格式化大小

    >>> format_size(10240)
    '10.00K'
    >>> format_size(1429365116108)
    '1.3T'
    >>> format_size(1429365116108000)
    '1.3P'
    """
    if size < 1024:
        return '%sB' % size
    elif size < 1024 **2:
        return '%.2fK' % (float(size) / 1024)
    elif size < 1024 ** 3:
        return '%.2fM' % (float(size) / 1024 ** 2)
    elif size < 1024 ** 4:
        return '%.2fG' % (float(size) / 1024 ** 3)
    elif size < 1024 ** 5:
        return '%.2fT' % (float(size) / 1024 ** 4)
    else:
        return "%.2fP" % (float(size) / 1024 ** 5)


def get_used_mem(format = True):
    p = psutil.Process(pid=os.getpid())
    mem_info = p.memory_info()
    if format:
        return format_size(mem_info.rss)
    else:
        return mem_info.rss

def mem_deco(name):
    def deco(func):
        def handle(*args, **kw):
            m1 = get_used_mem()
            try:
                return func(*args, **kw)
            finally:
                m2 = get_used_mem()
                print("%s mem (%s)->(%s)" % (name, m1, m2))
        return handle
    return deco

def prepare_kv_data(count:int, key_len:int, value_len:int):
    result = []
    for i in range(count):
        key = rand_str(key_len)
        value = rand_str(value_len)
        result.append((key, value))
    return result

class ResultPrinter:

    fmt = ""
    mem_before = ""
    mem_before_int = 0
    mem_after = ""
    mem_after_int = 0

    def print_head(self):
        heads = [
            ("operation", 10),
            ("times", 10),
            ("rt(ms)", 10),
            ("qps", 15),
            ("mem(before)", 11),
            ("mem(after)", 10),
            ("mem(used)", 10),
        ]

        fmt_list = []
        names = []
        lines = []

        for name, width in heads:
            fmt_list.append("%0" + str(width) + "s")
            names.append(name)
            lines.append("-" * width)

        self.fmt = " ".join(fmt_list)

        # print(self.fmt)
        # print(names)
        # print(lines)
        # print(tuple(names))

        print(self.fmt % tuple(names))
        print(self.fmt % tuple(lines))

    def print_result(self, operation, times, total_time):
        assert times > 0
        rt = total_time / times

        if total_time == 0:
            qps_str = "Inf"
        else:
            qps = times / total_time
            qps_str = "%.5f" % qps
        
        rt_str = "%.5f" % rt
        
        # print(fmt % ("operation", "times", "rt", "qps"))
        
        print(self.fmt % (operation, times, rt_str, qps_str, self.mem_before, self.mem_after, self.mem_used))

    def trace_start(self):
        self.mem_before = get_used_mem()
        self.mem_after = ""
        self.mem_before_int = get_used_mem(format=False)
    
    def trace_end(self):
        self.mem_after = get_used_mem()
        self.mem_after_int = get_used_mem(format=False)
        self.mem_used = format_size(self.mem_after_int - self.mem_before_int)

    def mem_deco(self, name):
        def deco(func):
            def handle(*args, **kw):
                m1 = get_used_mem()
                self.mem_before = m1
                self.mem_after = "-"
                try:
                    return func(*args, **kw)
                finally:
                    m2 = get_used_mem()
                    self.mem_after = m2
                    # print("%s mem (%s)->(%s)" % (name, m1, m2))
            return handle
        return deco

