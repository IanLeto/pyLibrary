# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 5:31 下午
# @Author  : Ian Leto
# @File    : options_cmd.py
# 干啥的    : 多参数 cmd 版本

import click


@click.command()
@click.option("--count", default=1, help="count")
@click.argument("name")
def hello(count, name):
    click.echo(count)
    click.echo(name)


if __name__ == '__main__':
    # 使用方式
    # python options_cmd.py --help
    # python options_cmd.py --count 10 ian
    hello()
