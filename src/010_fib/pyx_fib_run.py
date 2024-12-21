# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2022/01/26 16:35:01
# @modified 2022/01/26 16:35:13
# @filename pyx_fib.py

import pyximport

pyximport.install()

import fib

fib.run()