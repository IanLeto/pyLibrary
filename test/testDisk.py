# -*- coding: utf-8 -*-
# @Time    : 2021/12/8 5:30 下午
# @Author  : Ian Leto
# @File    : testDisk.py
# 干啥的    :

import json

if __name__ == '__main__':
    with open('/Users/ian/workdir/gamma/test') as file:
        file_old: str = file.read()
    with open('/Users/ian/workdir/gamma/testV2') as file2:
        file_new: str = file2.read()
    res_old = json.loads(file_old)['Data']
    res_new = json.loads(file_new)['Data']
    print(len(res_old))
    print(len(res_new))
    c: dict = {}
    data_old: dict = {v['IP']: v for v in res_old}
    data_new: dict = {v['IP']: v for v in res_new}
    count = 0
    for k, v in data_new.items():
        if k not in data_old.keys():
            print('new 多出来 k', k)
            continue
        if data_old[k]['Use'] != data_new[k]['Use'] or data_old[k]['Time'] != data_new[k]['Time']:
            count += 1
            print("new", k, v)
            print("old", k, data_old[k])
    # for k, v in data_old.items():
    #     if k not in data_new.keys():
    #         print('old 多出来 k', k)
    #         continue
    #     if data_new[k]['Use'] != data_old[k]['Use'] or data_new[k]['Time'] != data_old[k]['Time']:
    #         count += 1
    #         print("new", k, data_old[k])
    #         print("old", k, v)
    print(count)
