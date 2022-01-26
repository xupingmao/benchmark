from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("src/001_sum/pyx_sum1.pyx"),
    zip_safe=False,
)
