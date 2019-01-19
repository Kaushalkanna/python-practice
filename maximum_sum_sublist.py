def max_sum(input_list):
    current_max = input_list[0]
    global_max = input_list[0]
    for idx in range(1, len(input_list)):
        ele = input_list[idx]
        current_max = max(ele, current_max + ele)
        global_max = max(global_max, current_max)
    return global_max


print(max_sum([-1, 1, 2, -2, 3]))


def max_sum_sublist(input_list):
    current_max = input_list[0]
    global_max = input_list[0]
    current_max_list = [input_list[0]]
    global_max_list = [input_list[0]]
    for idx in range(1, len(input_list)):
        ele = input_list[idx]
        if ele > current_max + ele:
            current_max = ele
            current_max_list = [ele]
        else:
            current_max = current_max + ele
            current_max_list = current_max_list + [ele]
        if current_max > global_max:
            global_max = current_max
            global_max_list = current_max_list
    return global_max, global_max_list


print(max_sum_sublist([2, 1, -2, 3]))
