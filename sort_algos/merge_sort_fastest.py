def merge_sort(unsorted):
    start = []
    end = []
    while len(unsorted) > 1:
        a = min(unsorted)
        b = max(unsorted)
        start.append(a)
        end.append(b)
        unsorted.remove(a)
        unsorted.remove(b)
    if unsorted:
        start.append(unsorted[0])
    end.reverse()
    return start + end
