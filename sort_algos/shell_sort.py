def shell_sort(unsorted):
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(unsorted):
            temp = unsorted[i]
            j = i
            while j >= gap and unsorted[j - gap] > temp:
                unsorted[j] = unsorted[j - gap]
                j -= gap
            unsorted[j] = temp
            i += 1

    return unsorted
