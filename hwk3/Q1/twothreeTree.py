class node():
    def __init__(self, key, value, color=True, parent=None):
        self.key = key
        self.value = value
        self.color = color  # Black = True, Red = False
        self.l_child = None
        self.r_child = None
        self.parent = parent
        self.tomb = False


class twothree_tree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return not self.root

    def search(self, key, node=None):
        if self.isEmpty():
            return None, False
        # search the key in the tree
        # if the key has already been in the tree
        # we change value
        if not node:
            node = self.root

        if key == node.key and not node.tomb:
            return node, True
        if key == node.key and node.tomb:
            return node, False
        elif key < node.key and node.l_child:
            return self.search(key, node.l_child)
        elif key > node.key and node.r_child:
            return self.search(key, node.r_child)
        else:
            return node, False

    def insert(self, key, value):
        pos, isIn = self.search(key)

        if isIn:
            pos.value = value
            pos.tomb = False
            return

        # if return pos = None, the tree is empty
        # then we set the root
        if not pos:
            self.root = node(key, value)
            return

        # make a judgment to decide if this node is red of not
        if pos.color:  # Black
            # pos.color = False
            new_node = node(key, value, False, pos)
            if new_node.key < pos.key:
                pos.l_child = new_node
            else:
                pos.r_child = new_node
            return
        else:  # Red
            new_node = node(key, value, True, pos)
            if new_node.key < pos.key:
                pos.l_child = new_node
            else:
                pos.r_child = new_node
            return

    def delete(self, key):
        pos, isIn = self.search(key)
        if isIn:
            pos.tomb = True
        return