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


class Tree:
    pass


def ss():
    res = []

    def helper(tree: Tree):
        if not tree:
            return

        helper(tree.left)
        res.append(tree.val)
        helper(tree.right)

    helper(tree=Tree)
    return res


class node:
    pass


def slove(node1, node2):
    count = 0  # 进位
    head1, len1 = revert(node1)
    head2, len2 = revert(node2)
    if len1 < len2:
        head1, head2 = head2, head1
    cur1, cur2 = head1, head2
    while cur1 and cur2:
        if count > 0:
            cur1.val += cur2.val + count
            count = 0
        if cur1.val > 10:
            count += 1
        cur1 = cur1.next
        cur2 = cur2.next
    if count != 0:
        cur1.next = node(1)
    return revert(head1)


def revert(node):
    count = 0
    if not node:
        return None
    prev = node
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp
        count += 1

    return prev, count


if __name__ == '__main__':
    inp = input()

    c = int(inp)
    flag = True
    if c < 0:
        flag = False
    # inp = 1234567

    inp2 = input()
    l = inp2.split(" ")
    temp = str(inp)
    res = []
    for i in range(len(temp)):
        res.append(int(l[i]))
    if flag:

        r = ''.join(str(i) for i in res)
        print(r)
    else:
        r = ''.join(str(i) for i in res)
        print('-' + r)

# s = ''
# hash = {}
# for i in range(len(s)):
#     if s[i] not in hash:
#         hash[s[i]] = i
# res = -1
# for j in range(len(s)-1, -1, -1):
#     tem = j - hash[s[j]] - 1
#     if tem > res:
#         res = tem
# return res
