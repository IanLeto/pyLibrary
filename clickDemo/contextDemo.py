# -*- coding: utf-8 -*-
# @Time    : 2021/9/6 5:41 下午
# @Author  : Ian Leto
# @File    : contextDemo.py
# 干啥的    : click context

import click


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.option('--debug')
@click.pass_context
def run(ctx, debug):
    print(ctx.obj)
    click.echo('2', debug)


@click.command()
@click.option('--debug')
def sync(debug):
    click.echo(debug)


if __name__ == '__main__':
    run.add_command(sync)
    run()
