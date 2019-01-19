"""
Daily_Problem_42

This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24."""

import random


def quick_sort(unsorted, reverse=False):
    list_len = len(unsorted)

    if list_len <= 1:
        return unsorted

    pivot = unsorted[0]

    greater = [ele for ele in unsorted[1:] if ele > pivot]
    lesser = [ele for ele in unsorted[1:] if ele <= pivot]
    if reverse:
        return quick_sort(greater, reverse=True) + [pivot] + quick_sort(lesser, reverse=True)
    return quick_sort(lesser, reverse=True) + [pivot] + quick_sort(greater, reverse=True)


def solution(input_list, sum_total):
    sorted_list = quick_sort(input_list, reverse=True)
    print(sorted_list)
    output_list = []
    total = 0
    for ele in sorted_list:
        temp = total + ele
        if temp <= sum_total:
            output_list.append(ele)
            total = temp
    if total is sum_total and output_list:
        return output_list
    else:
        return


input_list = [
    ([random.randint(0, 100) for i in range(10)], random.randint(0, 100)),
    ([12, 1, 61, 5, 9, 2], 24),
    ([-2, -3, 4, -1, -2, 1, 5, -3], 12),
    ([-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7], 10)
]
for s, k in input_list:
    print(solution(s, k))
    print('*' * 15)
