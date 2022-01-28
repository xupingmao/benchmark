# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2022/01/28 23:15:27
# @modified 2022/01/28 23:19:47
# @filename pyx_run.py

import pyximport

pyximport.install()

import pyx_pystone as pystone

print(pystone)

pystone.run()
