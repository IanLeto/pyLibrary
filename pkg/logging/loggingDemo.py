# -*- coding: utf-8 -*-
# @Time    : 2021/9/14 5:50 下午
# @Author  : Ian Leto
# @File    : loggingDemo.py
# 干啥的    : logging demo

import logging

log_levels = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
}


def logging_hook(mode: str, file_path: str):
    logging.basicConfig(level=log_levels.get(mode, logging.DEBUG))
    logging.basicConfig(filename=file_path)


def do():
    logging_hook(mode='debug', file_path='demo')


if __name__ == '__main__':
    do()
    h = 'k'
    logging.debug("hello world %s", h)
