# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2022/01/26 16:59:18
# @modified 2022/01/26 17:12:31
# @filename dict_test2.pyx
# cython: language_level=3

import time
import random

def timeit(func, *args):
    t1 = time.time()
    ret = func(*args)
    cost_time = (time.time() - t1) * 1000
    print("cost time: %sms" % cost_time)

cdef str rand_str(int length):
    cdef str v
    cdef int a, b
    cdef int i

    v = ""
    a = ord('A')
    b = ord('Z')
    for i in range(length):
        v += chr(random.randint(a, b))
    return v

def test_random_gen(n):
    print("test_random_gen: n=%d" % n)
    for i in range(n):
        rand_str(5)

def test_dict_set(n):
    print("test_dict_set: n=%d" % n)
    d = dict()
    for i in range(n):
        key = rand_str(5)
        d[key] = 1
    print("len(dict)=%d" % len(d))

def test_dict_get(n):
    print("test_dict_get: n=%d" % n)
    cdef dict d = dict()
    cdef int i
    for i in range(n):
        key = rand_str(5)
        d[key] = 1
    print("len(dict)=%d" % len(d))

def run():
    timeit(test_random_gen, 100000)
    print("")
    timeit(test_dict_set, 100000)
    print("")
    timeit(test_dict_get, 100000)
