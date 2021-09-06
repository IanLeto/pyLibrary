# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 5:23 下午
# @Author  : Ian Leto
# @File    : hello.py
# 干啥的    : 基础的hello world

import click


@click.command()
def hello():
    click.echo('hello world')

if __name__ == '__main__':
    hello()