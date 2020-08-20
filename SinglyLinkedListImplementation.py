class Node(object):

    def __init__(self, value):
        self.value = value
        self.next_node = None


a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.next_node = c

print(a.value)
