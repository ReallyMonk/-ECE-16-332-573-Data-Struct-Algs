from read_file import read_file
import random


class Node():
    def __init__(self, value):
        self.value = value
        self.l_child = None
        self.r_child = None


class Tree():
    def __init__(self):
        self.root = None
        self.index = 0
        self.vals = []
        self.in_rank = 0

    def insert(self, value, node=None):
        new_node = Node(value)

        if not self.root:
            self.root = new_node
            return

        if not node:
            node = self.root

        if value < node.value:
            if not node.l_child:
                node.l_child = new_node
            else:
                self.insert(value, node.l_child)

        elif value > node.value:
            if not node.r_child:
                node.r_child = new_node
            else:
                self.insert(value, node.r_child)
        else:
            return

    def search(self, value, node=None):
        if not node:
            node = self.root

        if value == node.value:
            return node, True

        elif value < node.value:
            if node.l_child:
                return self.search(value, node.l_child)
            else:
                return node, False

        elif value > node.value:
            if node.r_child:
                return self.search(value, node.r_child)
            else:
                return node, False

    def traversal(self, node):
        self.index = self.index + 1

        if node.l_child:
            self.traversal(node.l_child)

        if node.r_child:
            self.traversal(node.r_child)

    def rank(self, value):
        self.vals = []
        #print(pos.parent.value)
        self.inOrderTr()

        return self.vals.index(7)

    def inOrderTr(self, node=None):
        if not node:
            node = self.root

        if node.l_child:
            self.inOrderTr(node.l_child)

        #print(node.value)
        #print(self.vals)
        #print(self.in_rank)
        self.vals.append(node.value)
        #if len(self.vals) == self.in_rank + 1:
        #    return self.vals[-1]

        if node.r_child:
            self.inOrderTr(node.r_child)

    def select(self, rank):
        self.vals = []
        self.in_rank = rank
        self.inOrderTr()
        return self.vals[rank]


nums = read_file()

tree = Tree()
for num in nums:
    # print(num)
    tree.insert(num)

rk = tree.rank(7)
slct = tree.select(7)

print(tree.vals)
print(slct, rk)