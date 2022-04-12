# -*- coding: utf-8 -*-
# @Time    : 2022/2/1 7:06 下午
# @Author  : Ian Leto
# @File    : sort.py
# 干啥的    :

#  冒泡
def sort1(arr: list):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)

    return arr


def sort_step1(arr: list):
    # 第一步 看作是找出最大值， 并将其丢到末尾
    n = len(arr)
    for j in range(n):
        if arr[j] > arr[j + 1]:
            swap(arr, j, j + 1)


# 这一步 最难抽象
def sort_step2(arr: list):
    # 第二步 对余下结点重新找最大值
    """

    n = len(arr)
    for j in range(n):
        if arr[j] > arr[j + 1]:
            swap(arr, j, j + 1)

    """


def swap(arr: list, i, j):
    arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    print(sort1([2, 3, 4, 1, 5, 67, 78]))
