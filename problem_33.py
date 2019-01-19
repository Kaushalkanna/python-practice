a = [2, 1, 5, 7, 2, 0, 5]


def solution(input_list):
    temp_list = []
    for element in input_list:
        temp_list.append(element)
        temp_list.sort()
        length = len(temp_list)
        middle = int(length / 2)
        if length is 1:
            print(temp_list[0])
        elif length % 2 is not 0:
            print(temp_list[middle])
        else:
            x = (temp_list[middle - 1] + temp_list[middle])/2
            y = str(x).split('.')
            if y[1] is '0':
                print(int(x))
            else:
                print(x)


solution(a)
