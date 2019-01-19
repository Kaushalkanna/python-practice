def reverse_list(l):
    if not l:
        return l
    front = 0
    back = len(l) - 1

    while front < back:
        temp = l[back]
        l[back] = l[front]
        l[front] = temp
        front += 1
        back -= 1
    return l


p = [i/2 for i in range(0, 1000)]

print(reverse_list(p))
