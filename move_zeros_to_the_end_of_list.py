def move_zeros1(l):
    count = 0
    print(len(l))
    for e in range(0, len(l)):
        if l[e] == 0:
            print(l)
            temp = l[e]
            l[e] = 'a'
            l.append(temp)
        count += 1
    l = [i for i in l if i != 'a']
    print(l)
    print(count)


def move_zeros2(l):
    count = 0
    print(len(l))
    for e in l:
        if e == 0:
            print(l)
            temp = e
            l.remove(e)
            l.append(temp)
        count += 1
    print(l)
    print(count)


def move_zeros3(l):
    count = 0
    print(len(l))
    for e in range(0, len(l)):
        if l[e] == 0:
            temp = l[e]
            l.pop(e)
            l.append(temp)
        count += 1
    print(l)
    print(count)


def move_zeros4(l):
    count = 0
    print(len(l))
    for e in range(0, len(l)):
        if l[e] == 0:
            p = e
            while p < len(l) and l[p] == 0:
                count += 1
                p += 1
            if p < len(l):
                temp = l[e]
                l[e] = l[p]
                l[p] = temp
        count += 1
    print(l)
    print(count)


move_zeros1([1, 0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 4, 0, 0, 0])

print('yo')

move_zeros2([1, 0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 4, 0, 0, 0])

print('hmm')

move_zeros3([1, 0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 4, 0, 0, 0])

print('maybe')

move_zeros4([1, 0, 0, 0, 0, 1, 2, 3, 4, 0, 0, 4, 0, 0, 0])
