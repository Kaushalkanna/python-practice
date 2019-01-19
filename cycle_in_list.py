def cycle_in_list(l):
    p = l[0]
    q = 0
    while True:
        if len(l) < p + 1 or len(l) < q + 1:
            return False
        p = l[p]
        if p == q:
            return True
        q = l[q]
        if p == q:
            return True


print(cycle_in_list([1, 2, 1, 4, 5, 6]))
