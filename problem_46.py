"""
Daily_Problem_46

This problem was asked by Amazon.

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length,
return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas"
is "anana".
"""


def solution(input_string):
    input_string_length = len(input_string)
    for length in range(input_string_length, 0, -1):
        for offset in range(0, input_string_length - length + 1):
            sub_string = input_string[offset:offset + length]
            if sub_string == sub_string[::-1]:
                return sub_string


print(solution('bananas'))
