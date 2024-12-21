import pyximport
import os

old_dirname = os.getcwd()

pyximport.install()
dirname = os.path.dirname(__file__)

os.chdir(dirname)

try:
    # 需要切换到当前目录
    import dict_test2
    dict_test2.run()
finally:
    os.chdir(old_dirname)
