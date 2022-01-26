# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2022/01/26 16:12:50
# @modified 2022/01/26 16:18:30
# @filename pyx_sum4.pyx
# cython: language_level=3, boundscheck=False
import sys
import time

def timeit(func, *args):
    t1 = time.time()
    ret = func(*args)
    t2 = time.time()
    cost_time = (t2-t1) * 1000
    print("cost_time:%sms" % cost_time)

def main():
    N = 500000
    result = 0

    cdef int i = 0
    for i in range(N):
        result += i

    print("loops=%d" % N)
    print("result=%d" % result)

def run():
    print("Only range optimized")
    timeit(main)

if __name__ == '__main__':
    run()