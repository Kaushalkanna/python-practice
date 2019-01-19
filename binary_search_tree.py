class Tree:
    def __init__(self, ele=None, left=None, right=None):
        self.node = ele
        self.left = left
        self.right = right

    def insert(self, ele):
        if not self.node:
            self.node = ele
        else:
            if ele < self.node:
                if not self.left:
                    self.left = Tree(ele)
                else:
                    self.left.insert(ele)
            else:
                if not self.right:
                    self.right = Tree(ele)
                else:
                    self.right.insert(ele)

    def print_tree_indented(self, level=0):
        if self.right:
            self.right.print_tree_indented(level + 1)
        print("    " * level + str(self.node))
        if self.left:
            self.left.print_tree_indented(level + 1)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.node)
        if self.right:
            self.right.print_tree()

    def print_tree_r_l(self):
        if self.right:
            self.right.print_tree_r_l()
        print(self.node)
        if self.left:
            self.left.print_tree_r_l()

left = Tree(125)
right = Tree(120)
t = Tree()
t.insert(10)
t.insert(12)
t.insert(20)
t.insert(18)
t.insert(4)
t.insert(6)
t.insert(2)
t.insert(25)
t.print_tree()
print("\n\n\n")
t.print_tree_indented()
print("\n\n\n")
t.print_tree_r_l()
