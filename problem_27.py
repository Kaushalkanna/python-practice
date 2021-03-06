from functools import reduce


def coding_problem_27(brace_yourself):
    """
    Given a string of round, curly, and square open and closing brackets, return whether the brackets are
    balanced (well-formed).
    # Examples:
    # >>> coding_problem_27('([])[]({})')
    # True
    # >>> coding_problem_27('([)]')
    # False
    # >>> coding_problem_27('((()')
    # False

    Note: I get it. This wants me to keep track of all opening parenthesis in a stack, and remove the top after
    encountering a closing one, provided it's of the matching type. Easy enough, BUT! such an algorithm requires lots of
    bookkeeping and it's inherently sequential. My implementation below works in a number of passes that only depends
    on the nesting levels of the braces; memory usage is O(n) for both solutions. Also, string operations are highly
    optimized, making this even faster.
    """
    copy = None
    while brace_yourself and brace_yourself != copy:
        copy = brace_yourself
        brace_yourself = reduce(lambda s, p: s.replace(p, ''), ['()', '{}', '[]'], brace_yourself)

    return brace_yourself == ''


print(coding_problem_27('([])[]({})'))
print(coding_problem_27('([)]'))
print(coding_problem_27('([{([()])}])'))
