from binarytree import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
print(root)

from binarytree import build

values = [10, 6, 4, 2, 12]
root1 = build(values)
print(root1)


class Tree:
    def __init__(self, cargo, left=None, right=None):
        self.cargo = cargo
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.cargo)


left = Tree(2)
right = Tree(3)
tree = Tree(1, left, right)


def total(t):
    if t is None: return 0
    return total(t.left) + total(t.right) + t.cargo




def print_tree(tree):
    if tree is None:
        return
    print(tree.cargo)
    print_tree(tree.left)
    print_tree(tree.right)


def print_tree_indented(tree, level=0):
    if tree is None: return
    print_tree_indented(tree.right, level+1)
    print("  " * level + str(tree.cargo))
    print_tree_indented(tree.left, level+1)

print_tree(tree)
print_tree_indented(tree)
