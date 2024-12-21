# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2022/01/26 16:35:51
# @modified 2022/01/26 16:36:46
# @filename pyx_fib2.py

import pyximport
import os

pyximport.install()
old_dirname = os.getcwd()
dirname = os.path.dirname(__file__)
os.chdir(dirname)

try:
    import fib2
    fib2.run()
except:
    os.chdir(old_dirname)
