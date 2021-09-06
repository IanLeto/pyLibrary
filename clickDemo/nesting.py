# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 5:29 下午
# @Author  : Ian Leto
# @File    : nesting.py
# 干啥的    :
import click


@click.group()
def nesting():
    pass


@click.command()
def nesting1():
    pass


@click.command()
def nesting2():
    pass


if __name__ == '__main__':
    nesting.add_command(nesting1)
    nesting.add_command(nesting2)
