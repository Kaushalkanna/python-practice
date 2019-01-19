"""
Daily_Problem_44

This problem was asked by Google.

We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements
A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions:
(2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.
"""
import random


def solution(input_list):
    temp = list(zip(input_list, range(len(input_list))))
    sorted_data = sorted(temp)
    sorted_indices = [a[1] for a in sorted_data]

    inversions = 0
    for index in range(len(sorted_indices)):
        destination = sorted_indices.index(index)
        sorted_indices.remove(index)
        inversions += destination

    return inversions


input_list = [
    [random.randint(0, 100) for i in range(10)],
    [2, 4, 1, 3, 5],
    [-2, -3, 4, -1, -2, 1, 5, -3],
    [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
]

for ele in input_list:
    print(solution(ele))
    print('*' * 15)
