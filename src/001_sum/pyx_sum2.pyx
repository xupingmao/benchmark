# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2022/01/26 10:25:00
# @modified 2022/01/26 16:20:05
# @filename pyx_sum2.pyx
# cython: language_level=3

import sys
import time

def timeit(func, *args):
    t1 = time.time()
    ret = func(*args)
    t2 = time.time()
    cost_time = (t2-t1) * 1000
    print("cost_time:%sms" % cost_time)

def main():
    cdef int i = 0
    cdef long N = 500000
    cdef long result = 0

    # i必须定义为int，不然优化粒度不大
    for i in range(N):
        result += i

    print("loops=%d" % N)
    print("result=%d" % result)

def run():
    print("Full optimized")
    timeit(main)

if __name__ == '__main__':
    run()