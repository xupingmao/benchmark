# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2022/01/26 10:25:00
# @modified 2022/01/26 16:41:47
# @filename fib2.pyx
# cython: language_level=3

import sys
import time

cdef int fib(int n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

def timeit(func, *args):
    t1 = time.time()
    ret = func(*args)
    t2 = time.time()
    cost_time = (t2-t1) * 1000
    print("cost_time:%sms" % cost_time)

def main():
    result = fib(30)
    print("fib(30)=%d" % result)

def run():
    timeit(main)

if __name__ == '__main__':
    run()