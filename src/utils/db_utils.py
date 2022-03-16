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


def get_used_mem():
    p = psutil.Process(pid=os.getpid())
    mem_info = p.memory_info()
    return format_size(mem_info.rss)

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
