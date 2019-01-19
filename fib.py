def fib(n):
    fib_data = [1,1]
    if n == 1 or n == 2:
        return fib_data[n-1]
    for i in range(2,n):
        fib_data.append(fib_data[i-1] + fib_data[i-2])
    return fib_data[n-1]

print(fib(100))
