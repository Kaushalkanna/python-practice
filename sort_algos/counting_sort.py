def counting_sort(unsorted):
    if not unsorted:
        return []

    # get some information about the unsorted
    coll_len = len(unsorted)
    coll_max = max(unsorted)
    coll_min = min(unsorted)

    # create the counting array
    counting_arr_length = coll_max + 1 - coll_min
    counting_arr = [0] * counting_arr_length

    # count how much a number appears in the unsorted
    for number in unsorted:
        counting_arr[number - coll_min] += 1

    # sum each position with it's predecessors. now, counting_arr[i] tells
    # us how many elements <= i has in the unsorted
    for i in range(1, counting_arr_length):
        counting_arr[i] = counting_arr[i] + counting_arr[i - 1]

    # create the output unsorted
    ordered = [0] * coll_len

    # place the elements in the output, respecting the original order (stable
    # sort) from end to begin, updating counting_arr
    for i in reversed(range(0, coll_len)):
        ordered[counting_arr[unsorted[i] - coll_min] - 1] = unsorted[i]
        counting_arr[unsorted[i] - coll_min] -= 1

    return ordered


def counting_sort_string(string):
    return ''.join([chr(i) for i in counting_sort([ord(c) for c in string])])
