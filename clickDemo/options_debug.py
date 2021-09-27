# -*- coding: utf-8 -*-
# @Time    : 2021/9/16 3:06 下午
# @Author  : Ian Leto
# @File    : options_debug.py
# 干啥的    :

import click


# 基础语法
@click.command()
@click.option("--count", default=1, help="count")
@click.argument("name")
def hello(count, name):
    click.echo(count)
    click.echo(name)


#


if __name__ == '__main__':
    hello(['--count', 10, 'ian'])
