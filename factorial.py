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

print(factorial_easy(2))