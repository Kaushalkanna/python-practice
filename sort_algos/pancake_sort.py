def pancake_sort(unsorted):
    cur = len(unsorted)
    while cur > 1:
        mi = unsorted.index(max(unsorted[0:cur]))
        unsorted = unsorted[mi::-1] + unsorted[mi + 1:len(unsorted)]
        unsorted = unsorted[cur - 1::-1] + unsorted[cur:len(unsorted)]
        cur -= 1
    return unsorted
