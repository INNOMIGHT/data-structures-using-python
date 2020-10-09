class Node:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)

        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)

        else:
            print("Value already in tree!")

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)

    def _height(self, cur_level, tree_height):
        if cur_level is None:
            return tree_height
        left_height = self._height(cur_level.left_child, tree_height + 1)
        right_height = self._height(cur_level.right_child, tree_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(value, self.root)

    def _search(self, value, cur_node):
        if cur_node.value == value:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._search(value, cur_node.right_child)
        else:
            return False

    def delete_value(self, value):
        return self.delete_node(self.search(value))

    def delete_node(self, node):

        def min_value(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        def children_present(n):
            num_children = 0
            if n.left_child is not None:
                num_children += 1
            if n.right_child is not None:
                num_children += 1
            return num_children

        node_parent = node.parent

        num_children_present = children_present(node)

        if num_children_present == 0:
            if node_parent.left_child == node:
                node_parent.left_child = None
            else:
                node_parent.right_child = None

        elif num_children_present == 1:
            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent.left_child == node:
                node_parent.left_child = child
            else:
                node_parent.right_child = child

            child.parent = node_parent

        if num_children_present == 2:
            successor = min_value(node.right_child)

            node.value = successor.value

            self.delete_node(successor)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)


my_tree = BinarySearchTree()
my_tree.insert(5)
my_tree.insert(4)
my_tree.insert(7)
my_tree.insert(2)
my_tree.insert(1)

my_tree.print_tree()
print("Height of the Tree is " + str(my_tree.height()))
print(my_tree.search(4))
print(my_tree.search(9))
