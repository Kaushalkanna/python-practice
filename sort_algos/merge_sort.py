def merge_sort(unsorted):
    length = len(unsorted)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(unsorted[:midpoint])
        right_half = merge_sort(unsorted[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                unsorted[k] = left_half[i]
                i += 1
            else:
                unsorted[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            unsorted[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            unsorted[k] = right_half[j]
            j += 1
            k += 1

    return unsorted

import random

a = [random.randint(-100, 100) for i in range(100)]
print(merge_sort(a))
