def insertion_sort(unsorted):
    for index in range(1, len(unsorted)):
        while index > 0 and unsorted[index - 1] > unsorted[index]:
            unsorted[index], unsorted[index - 1] = unsorted[index - 1], unsorted[index]
            index -= 1

    return unsorted
