class BinaryTree(object):

    def __init__(self, rootObj):
        self.key = rootObj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if(self.left_child is None):
            self.left_child = BinaryTree(new_node)

        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if(self.right_child is None):
            self.right_child = BinaryTree(new_node)

        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key
