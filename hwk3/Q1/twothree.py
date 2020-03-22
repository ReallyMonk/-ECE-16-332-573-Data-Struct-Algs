class node():
    def __init__(self, node_type, kv_pair, parent=None, children=None):
        self.is2node = node_type
        self.parent = parent
        self.children = children
        self.l_child = None
        self.r_child = None
        self.m_child = None

        #print(kv_pair)

        if children:
            self.l_child = children[0]
            self.r_child = children[-1]

        if self.is2node:
            k, = kv_pair
            v, = kv_pair.values()
            self.key = k
            self.value = v
        else:
            if children:
                self.m_child = children[1]
            l_k, = kv_pair[0]
            l_v, = kv_pair[0].values()
            r_k, = kv_pair[1]
            r_v, = kv_pair[1].values()
            self.l_key = l_k
            self.r_key = r_k
            self.l_value = l_v
            self.r_value = r_v


class twothree_tree():
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root

    def search(self, key, node=None):
        print('search for ', key)
        # if the tree is empty or not
        if not self.isEmpty():
            return 'root', False
        # if no node is input, then search on root node
        if not node:
            node = self.root

        # make a judgement about the node
        if node.is2node:
            if key == node.key:
                return node, True
            elif key < node.key and node.l_child:
                return self.search(key, node.l_child)
            elif key > node.key and node.r_child:
                return self.search(key, node.r_child)
            else:
                return node, False
        else:
            if key == node.l_key or key == node.r_key:
                return node, True
            elif key < node.l_key and node.l_child:
                return self.search(key, node.l_child)
            elif key > node.l_key and key < node.r_key and node.m_child:
                return self.search(key, node.m_child)
            elif key > node.r_key and node.r_child:
                return self.search(key, node.r_child)
            else:
                return node, False

    def insert(self, key, pos=None):
        # create a new 2-node with key
        if type(key) == node:
            k_node = key
        else:
            k_node = node(True, key)

        is_in = False
        if not pos:
            pos, is_in = self.search(k_node.key)

            # if the tree is empty set root
            if not is_in and pos == 'root':
                print('set root now')
                self.root = node(True, key)
                print('done')
                return

            # first we need to know if we have our key inside the tree
            # if we do, we change the value
            # if not, we insert a new value
            if is_in:
                print('change value')
                k, = key
                v, = key.values()
                if pos.is2node:
                    pos.value = v
                else:
                    if pos.l_key == k:
                        pos.l_value = v
                    else:
                        pos.r_value = v
                print('done')
                return

        if pos.is2node:
            print('insert a 2node')
            print('insert ', k_node.key, ' into ', pos.key)
            # set keys and children up
            if k_node.key < pos.key:
                keys = [{k_node.key: k_node.value}, {pos.key: pos.value}]
                children = [k_node.l_child, k_node.r_child, pos.r_child]
            else:
                keys = [{pos.key: pos.value}, {k_node.key: k_node.value}]
                children = [pos.l_child, k_node.l_child, k_node.r_child]
            # set parent up
            new_node = node(False, keys, pos.parent, children)

            if children[0]:
                for child in children:
                    child.parent = new_node

            # if pos has no parent, it is root
            if not pos.parent:
                self.root = new_node
                print('done')
                return

        else:
            # transform to a new node
            print('insert a 3node')
            print('insert ', k_node.key, ' into ', pos.l_key, 'and', pos.r_key)
            if k_node.key < pos.l_key:
                l_new = k_node
                r_new = node(True, {pos.r_key: pos.r_value}, None,
                             [pos.m_child, pos.r_child])
                new_node = node(True, {pos.l_key: pos.l_value}, None,
                                [l_new, r_new])
                l_new.parent = new_node
                r_new.parent = new_node
                if pos.parent:
                    self.insert(new_node, pos.parent)
                else:
                    self.root = new_node
                    print('done')
                    return

            elif k_node.key > pos.r_key:
                l_new = node(True, {pos.l_key: pos.l_value}, None,
                             [pos.l_child, pos.m_child])
                r_new = k_node
                new_node = node(True, {pos.r_key: pos.r_value}, None,
                                [l_new, r_new])
                l_new.parent = new_node
                r_new.parent = new_node
                if pos.parent:
                    print(pos.parent)
                    self.insert(new_node, pos.parent)
                else:
                    self.root = new_node
                    print('done')
                    return

            else:
                l_new = node(True, {pos.l_key: pos.l_value}, None,
                             [pos.l_child, k_node.l_child])
                r_new = node(True, {pos.r_key: pos.r_value}, None,
                             [pos.r_child, k_node.r_child])
                new_node = node(True, k_node.key, None, [l_new, r_new])
                l_new.parent = new_node
                r_new.parent = new_node
                if pos.parent:
                    print(pos.parent)
                    self.insert(new_node, pos.parent)
                else:
                    self.root = new_node
                    print('done')
                    return


_23tree = twothree_tree()

test = [{
    'S': 0
}, {
    'E': 1
}, {
    'A': 2
}, {
    'R': 3
}, {
    'C': 4
}, {
    'H': 5
}, {
    'E': 6
}, {
    'X': 7
}, {
    'A': 8
}, {
    'M': 9
}, {
    'P': 10
}, {
    'L': 11
}, {
    'E': 12
}]

for a in test:
    _23tree.insert(a)

pos, is_in = _23tree.search('A')
print(pos.value)
print(_23tree.root.key)
