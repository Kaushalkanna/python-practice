def longest(seq):
    count = 0
    max_count = 0
    longest_char = None
    previous = None
    for char in seq:
        if previous == char:
            count += 1
            if count > max_count:
                max_count = count
                longest_char = char
        else:
            count = 1
        previous = char
    return {longest_char: max_count}
    pass

print(longest('aaaaaaaaaaaaaaaaaaaaaaaaaabbbaaabbbbccccccddddeeeeeeeeeeeeeeee'))
