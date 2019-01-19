class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node is not None:
            print(node.val)
            node = node.next

    def remove_duplicates(self):
        elements = []
        node = self
        previous = None
        while node is not None:
            if node.val in elements:
                previous.next = node.next
            else:
                elements.append(node.val)
            previous = node
            node = node.next


header_node = Node(3)
node1 = Node(2)
node2 = Node(1)
node3 = Node(1)
node4 = Node(2)
node5 = Node(5)


header_node.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

header_node.remove_duplicates()
header_node.traverse()
