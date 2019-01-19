def selection_sort(unsorted):
    length = len(unsorted)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if unsorted[k] < unsorted[least]:
                least = k
        unsorted[least], unsorted[i] = unsorted[i], unsorted[least]
    return unsorted
