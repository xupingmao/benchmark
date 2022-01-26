# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2022/01/26 14:52:33
# @modified 2022/01/26 16:10:22
# @filename pyx_sum3_run.py
"""通过pyximport导入模块"""

import pyximport

pyximport.install()

import pyx_sum2 as sum2

sum2.run()