def BinaryTree(r):
    return ([r, [], []])


def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])

    else:
        root.insert(1, [newBranch, [], []])

    return root


def insertRight(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t)

    else:
        root.insert(2, [newBranch, [], []])

    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]