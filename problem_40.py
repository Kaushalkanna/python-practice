"""
Daily_Problem_40

This problem was asked by Google.

Given an array of integers where every integer occurs three times except for one integer,
which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""


def solution(input_list):
    a = 3 * sum(set(input_list))
    b = sum(input_list)
    return (a - b) // 2


def solution1(input_list):
    n = len(input_list)
    ones = 0
    twos = 0

    for i in range(n):
        twos = twos | (ones & input_list[i])
        ones = ones ^ input_list[i]
        common_bit_mask = ~(ones & twos)
        ones &= common_bit_mask
        twos &= common_bit_mask
    return ones


a = [12, 1, 12, 3, 12, 1, 1, 2, 3, 2, 2, 3, 7]
print(solution(a))
print(solution1(a))
