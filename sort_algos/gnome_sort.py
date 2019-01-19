def gnome_sort(unsorted):
    if len(unsorted) <= 1:
        return unsorted

    i = 1

    while i < len(unsorted):
        if unsorted[i - 1] <= unsorted[i]:
            i += 1
        else:
            unsorted[i - 1], unsorted[i] = unsorted[i], unsorted[i - 1]
            i -= 1
            if i == 0:
                i = 1

    return unsorted
