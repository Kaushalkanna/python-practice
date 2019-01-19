"""
Daily_Problem_48

This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of
'+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
"""
from PIL.ImageMath import ops


class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def in_order_traversal(self, root_node):
        res = None
        if not root_node.left and not root_node.right:
            return root_node.data
        if root_node:
            res1 = ()
            res1 += (self.in_order_traversal(root_node.left),)
            res1 += (root_node.data,)
            res = res1 + (self.in_order_traversal(root_node.right),)
        return res

    def pre_order_traversal(self, root_node):
        res = None
        if not root_node.left and not root_node.right:
            return root_node.data
        if root_node:
            res1 = ()
            res1 += (root_node.data,)
            res1 += (self.in_order_traversal(root_node.left),)
            res = res1 + (self.in_order_traversal(root_node.right),)
        return res

    def post_order_traversal(self, root_node):
        res = []
        if root_node:
            res = self.post_order_traversal(root_node.left)
            res = res + self.post_order_traversal(root_node.right)
            res.append(root_node.data)
        return res


root = Node()
root.data = '*'

root.left = Node()
root.left.data = '+'

root.left.left = Node()
root.left.left.data = 3

root.left.right = Node()
root.left.right.data = 2

root.right = Node()
root.right.data = '+'

root.right.left = Node()
root.right.left.data = 4

root.right.right = Node()
root.right.right.data = 5

traversal_data = root.in_order_traversal(root)
print(root.pre_order_traversal(root))


def solution(data):
    if not isinstance(data, tuple):
        return data

    left, op, right = data
    op2fun = {'+': ops.add, '-': ops.sub, '*': ops.mul, '/': ops.truediv}
    return op2fun[op](solution(left), solution(right))


# print(solution(traversal_data))
