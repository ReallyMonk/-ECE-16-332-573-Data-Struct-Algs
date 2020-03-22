# from twothreeTree import node
from twothreeTree import twothree_tree


class ST():
    def __init__(self):
        self.s_t = twothree_tree()
        self.keys_set = []

    def inOrderTraversal(self, node=None):
        if not node:
            node = self.s_t.root

        if node.l_child:
            self.inOrderTraversal(node.l_child)

        self.keys_set.append(node.key)

        if node.r_child:
            self.inOrderTraversal(node.r_child)

        return

    def get(self, key):
        tar, isIn = self.s_t.search(key)
        if isIn:
            return tar.value
        else:
            return None

    def put(self, key, value):
        self.s_t.insert(key, value)
        return

    def delete(self, key):
        self.s_t.delete(key)

    def contain(self, key):
        tar, isIn = self.s_t.search(key)
        return isIn

    def isEmpty(self):
        return self.s_t.isEmpty()

    def size(self):
        self.keys_set = []
        self.inOrderTraversal()
        return len(self.keys)

    def keys(self):
        self.keys_set = []
        self.inOrderTraversal()
        return self.keys_set


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

k = []
v = []
for i in test:
    k.append(list(i.keys())[0])
    v.append(list(i.values())[0])

table = ST()
for key, value in zip(k, v):
    table.put(key, value)

print(table.keys())
