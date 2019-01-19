"""
Daily_Problem_49

This problem was asked by Amazon.

Given an array of numbers, find the maximum sum of any contiguous subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements
42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
"""

from copy import copy


def solution(input_list):
    max_sum = 0
    max_ending_here = 0
    for ele in input_list:
        max_ending_here = max_ending_here + ele
        if max_ending_here < 0:
            max_ending_here = 0
        if max_sum < max_ending_here:
            max_sum = max_ending_here

    return max_sum


def solution1(input_list):
    max_sum = input_list[0]
    curr_max = input_list[0]

    temp_list = copy(input_list)
    start_index, max_start_index = 0, 0
    end_index, max_end_index = 0, 0
    del (temp_list[0])
    for ele in temp_list:
        curr_max += ele
        if curr_max < ele:
            curr_max = ele
            start_index = input_list.index(ele)
        end_index = input_list.index(ele)
        if max_sum < curr_max:
            max_sum = curr_max
            max_start_index = start_index
            max_end_index = end_index

    return max_sum, max_start_index, max_end_index, input_list[max_start_index: max_end_index + 1]


def solution2(input_list):
    max_sum = input_list[0]
    curr_max = input_list[0]
    start_index, max_start_index, end_index, max_end_index = 0, 0, 0, 0

    for i in range(1, len(input_list)):

        curr_max += input_list[i]
        if curr_max < input_list[i]:
            curr_max = input_list[i]
            start_index = i
        end_index = i
        if max_sum < curr_max:
            max_sum = curr_max
            max_start_index = start_index
            max_end_index = end_index

    return max_sum, max_start_index, max_end_index, input_list[max_start_index: max_end_index + 1]


input_list = [
    [34, -50, 42, 14, -5, 86],
    [-5, -1, -8, -9],
    [-2, -3, 4, -1, -2, 1, 5, -3],
    [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
]

for ele in input_list:
    print(solution(ele))
    print(solution1(ele))
    print(solution1(ele))
    print('*' * 15)
