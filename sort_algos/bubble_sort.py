def bubble_sort(unsorted):
    length = len(unsorted)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if unsorted[j] > unsorted[j + 1]:
                swapped = True
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]
        if not swapped:
            break  # Stop iteration if the unsorted is sorted.
    return unsorted
