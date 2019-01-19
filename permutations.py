def to_string(l):
    return ''.join(l)


def permute(input_list, start_index, end_index, result_data):
    if start_index == end_index:
        result_data.append(to_string(input_list))
    else:
        for i in range(start_index, end_index):
            input_list[start_index], input_list[i] = input_list[i], input_list[start_index]
            permute(input_list, start_index + 1, end_index, result_data)
            input_list[start_index], input_list[i] = input_list[i], input_list[start_index]  # backtrack
    return result_data


string = "ABC"
a = list(string)
result = []
print(permute(a, 0, len(a), result))
