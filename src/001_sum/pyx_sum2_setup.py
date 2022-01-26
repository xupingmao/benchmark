# -*- coding:utf-8 -*-
# @author xupingmao
# @since 2022/01/26 14:11:34
# @modified 2022/01/26 16:10:31
# @filename pyx_sum2_setup.py

from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("src/001_sum/pyx_sum2.pyx"),
    zip_safe=False,
)
