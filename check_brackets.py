class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None

    def push(self, n):
        self.items.append(n)

    def is_empty(self):
        return self.items == []

    def print_stack(self):
        print(self.items)

    def stack_len(self):
        return len(self.items)


m = '({)[]}'


def check_brackets(string):
    open_brackets = {
        '(': True,
        '{': True,
        '[': True
    }

    close_brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    s = Stack()
    for b in string:
        if open_brackets.get(b):
            s.push(b)
        else:
            t = s.pop()
            if t == close_brackets.get(b):
                pass
            else:
                return False

    if s.stack_len() > 0:
        return False
    return True


print(check_brackets('[{}'))
