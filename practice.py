# #!/bin/python3
#
#
# # Complete the hourglassSum function below.
# def hourglassSum(a):
#     max_sum = None
#     for i in range(len(a)):
#         for j in range(len(a[i])):
#             if (i + 2) < len(a) and (j + 2) < len(a):
#                 r = a[i][j] + a[i][j + 1] + a[i][j + 2] + a[i + 1][j + 1] + a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][
#                     j + 2]
#                 max_sum = r if max_sum is None else max(max_sum, r)
#
#     return max_sum
#
#
# if __name__ == '__main__':
#     print(hourglassSum(
#             [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0],
#              [0, 0, 1, 2, 4, 0]]
#     ))


def arrayManipulation(n, queries):
    a = [0] * (n + 1)
    for inp in queries:
        x, y, incr = inp[0], inp[1], inp[2]
        a[x - 1] += incr
        if y <= len(a):
            a[y] -= incr
    max_sum = x = 0
    for i in a:
        x = x + i
        if max_sum < x:
            max_sum = x
    return max_sum


print(arrayManipulation(10, [[2, 6, 8], [3, 5, 7], [1, 8, 1], [5, 9, 15]]))
