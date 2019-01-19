def quick_sort(unordered):
    list_length = len(unordered)

    if list_length <= 1:
        return unordered

    pivot = unordered[0]
    greater_list = [ele for ele in unordered[1:] if ele > pivot]
    smaller_list = [ele for ele in unordered[1:] if ele <= pivot]
    return quick_sort(greater_list) + [pivot] + quick_sort(smaller_list)


def quick_sort2(unordered):
    list_length = len(unordered)

    if list_length <= 1:
        return unordered

    pivot = unordered[0]
    del unordered[0]
    greater_list = []
    smaller_list = []
    for ele in unordered:
        if ele > pivot:
            greater_list.append(ele)
        else:
            smaller_list.append(ele)
    return quick_sort(greater_list) + [pivot] + quick_sort(smaller_list)


import random

a = [random.randint(0, 100) for i in range(100)]
print(a)
m = (quick_sort(a))
n = (quick_sort2(a))
print(n)
print(len(n))
if m == n:
    print('Yeah')

else:
    print('Nope')
