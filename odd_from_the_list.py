def find_odd(l):
    counts = {}
    for e in l:
        if counts.get(e):
            counts.pop(e)
        else:
            counts[e] = 1
    for count in counts:
        print(count)


find_odd([1, 2, 3, 4, 5, 1, 2, 3, 4])
