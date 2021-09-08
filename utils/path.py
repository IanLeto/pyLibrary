# -*- coding: utf-8 -*-
# @Time    : 2021/9/8 7:16 下午
# @Author  : Ian Leto
# @File    : path.py
# 干啥的    : 路径相关方法

import os

# 获取路径方式 eg utils/path/testPath
rootPath = os.path.abspath('..')


def get_root_path():
    return os.path.abspath('..')


def get_file_path(path: str):
    return os.path.join(get_root_path(), path)


# 当前路径
os.getcwd()

# 上级路径
os.path.abspath('..')

if __name__ == '__main__':
    print(os.path.abspath('hello.py'))
    print(os.getcwd())
