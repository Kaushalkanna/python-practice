def to_string(l):
    return ''.join(l)


def permute(a, l, r):
    if l == r:
        print to_string(a)
    else:
        for i in xrange(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)


def factorial(k):
    p = 1
    for i in range(k, 1, -1):
        p += p * (i - 1)
    return p

print(factorial(2))


def factorial_easy(k):
    p = k
    for i in range(k-1, 1, -1):
        p *= i
    return p

print(factorial_easy(6))


