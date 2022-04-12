# -*- coding: utf-8 -*-
# @Time    : 2022/1/24 5:38 下午
# @Author  : Ian Leto
# @File    : tr2.py
# 干啥的    : 字符串
k = "My name is %s and my age is %d years old!" % ('Bob', 30)

# 分割字符串
a = 'xx-sd-xx-json'


def sp(s: str):
    res = str.split(s, '-')
    if len(res) > 2:
        return "-".join(res[0:len(res) - 1])
    return s


import jinja2

p = '{"name":{{ name }}, "test": {{ xxx.xx2 | safe }}}'
dic = {'name': 'k', "xxx2": {"xx": "safe"}}
res = jinja2.Template(p).render(dic)
print(res)

if __name__ == '__main__':
    print(sp(a))
