# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2022/01/26 10:25:00
# @modified 2022/01/26 10:32:43
# @filename sum.py
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
    for i in range(N):
        result += i

    print("loops=%d" % N)
    print("result=%d" % result)

if __name__ == '__main__':
    timeit(main)