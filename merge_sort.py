import random


def merge_sort(unsorted):
    unsorted_len = len(unsorted)
    if unsorted_len <= 1:
        return unsorted, 0

    mid_len = unsorted_len // 2
    left_unsorted, left_i = merge_sort(unsorted[:mid_len])
    right_unsorted, right_i = merge_sort(unsorted[mid_len:])

    left_unsorted_len = len(left_unsorted)
    right_unsorted_len = len(right_unsorted)

    i, j, k = 0, 0, 0

    inversions = left_i + right_i

    while i < left_unsorted_len and j < right_unsorted_len:
        if left_unsorted[i] < right_unsorted[j]:
            unsorted[k] = left_unsorted[i]
            i += 1
        else:
            unsorted[k] = right_unsorted[j]
            j += 1
            inversions += left_unsorted_len - i
        k += 1

    while i < left_unsorted_len:
        unsorted[k] = left_unsorted[i]
        i += 1
        k += 1

    while j < right_unsorted_len:
        unsorted[k] = right_unsorted[j]
        j += 1
        k += 1

    return unsorted, inversions


a = list(range(1, 101))
random.shuffle(a)
print(a)
b = sorted(a)
c, inversions = merge_sort(a)
print(b == c)
print(c)
print(len(c), inversions)
