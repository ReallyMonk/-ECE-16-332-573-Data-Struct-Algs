import random


class Node():
    def __init__(self, value):
        self.value = value
        self.l_child = None
        self.r_child = None


class tree():
    def __init__(self):
        self.root = None
        self.depth = []
        self.now_deep = 0

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

    def cnt_depth(self, node=None):
        if not node:
            node = self.root

        self.now_deep = self.now_deep + 1

        if not node.l_child and not node.r_child:
            self.depth.append(self.now_deep)

        if node.l_child:
            self.cnt_depth(node.l_child)

        if node.r_child:
            self.cnt_depth(node.r_child)

        self.now_deep = self.now_deep - 1


srt = []
srt_avg = []
rdm = []
rdm_avg = []
for i in range(10):
    sorted_seq = list(range(2**i))
    random_seq = list(range(2**i))
    random.shuffle(random_seq)

    #print(sorted_seq, random_seq)

    sorted_tree = tree()
    random_tree = tree()

    for s in sorted_seq:
        sorted_tree.insert(s)
    sorted_tree.cnt_depth()
    s_depth = sorted_tree.depth
    srt.append(s_depth)
    srt_avg.append(sum(s_depth)/len(s_depth))

    for r in random_seq:
        random_tree.insert(r)
    random_tree.cnt_depth()
    r_depth = random_tree.depth
    rdm.append(r_depth)
    rdm_avg.append(sum(r_depth)/len(r_depth))

print(srt, srt_avg)
print(rdm, rdm_avg)