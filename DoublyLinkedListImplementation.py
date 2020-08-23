class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = Node(2)
b = Node(3)
c = Node(4)

a.next_node = b
b.next_node = c
c.next_node = None
b.prev_node = a
c.prev_node = b

