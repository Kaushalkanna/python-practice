def quick_sort(unsorted):

    list_length = len(unsorted)

    if list_length <= 1:
        return unsorted

    pivot = unsorted[0]
    greater = [element for element in unsorted[1:] if element > pivot]
    lesser = [element for element in unsorted[1:] if element <= pivot]
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


import random

a = [random.randint(0, 100) for i in range(100)]
print(a)
print(quick_sort(a))
