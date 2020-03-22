# a balanced left lean red black tree
class RB_node():
    def __init__(self, key, color=False):
        self.key = key
        self.color = color  # Red = False, Black = True
        self.l_child = None
        self.r_child = None
        self.parent = None


class LLRB_tree():
    def __init__(self):
        self.root = None
        self.total_node = 0
        self.red_node = 0

    def isRed(self, node):
        if node:
            return not node.color
        else:
            return False

    def setRed(self, node):
        if node.color:
            self.red_node = self.red_node + 1
        node.color = False
    
    def setBlack(self, node):
        if not node.color:
            self.red_node = self.red_node - 1
        node.color = True

    def left_rotate(self, node):
        p = node.parent
        r = node.r_child

        node.r_child = r.l_child
        if node.r_child:
            node.r_child.parent = node

        r.l_child = node
        node.parent = r

        r.parent = p
        if not p:
            self.root = r
        else:
            if p.l_child == node:
                p.l_child = r
            else:
                p.r_child = r
        pass

    def right_rotate(self, node):
        p = node.parent
        l = node.l_child

        node.l_child = l.r_child
        if node.l_child:
            node.l_child.parent = node

        l.r_child = node
        node.parent = l

        l.parent = p
        if not p:
            self.root = l
        else:
            if p.l_child == node:
                p.l_child = l
            else:
                p.r_child = l
        pass

    def search(self, key, node=None):
        # print(key)
        if not node:
            node = self.root

        # print(node.key)

        if key < node.key and node.l_child:
            #print(node.key, node.l_child.key)
            # print('l_child')
            return self.search(key, node.l_child)
        elif key > node.key and node.r_child:
            # print('r_child')
            return self.search(key, node.r_child)
        else:
            return node

    def insert(self, key):
        #print('insert', key)
        # for root insertion
        if not self.root:
            self.root = RB_node(key, True)
            self.total_node = self.total_node + 1
            return

        pos = self.search(key)
        new_node = RB_node(key)

        if key < pos.key:
            pos.l_child = new_node
            new_node.parent = pos
        else:
            pos.r_child = new_node
            new_node.parent = pos

        self.total_node = self.total_node + 1
        self.red_node = self.red_node + 1
        self.fix(new_node)
        return

    def fix(self, node):

        while node.parent:
            prt = node.parent
            # if prt is black
            if prt.color:
                # if node is right child
                if node.key > prt.key:
                    # if brother exist and is red
                    if self.isRed(prt.l_child):
                        self.setRed(prt)
                        self.setBlack(node)
                        self.setBlack(prt.l_child)
                        node = prt
                        continue
                    # if no brother exist or is balck
                    else:
                        self.left_rotate(prt)
                        self.setBlack(node)
                        self.setRed(prt)
                        break
                # if node is left child
                else:
                    break
            # if prt is Red
            else:
                # if node is r_child
                if node.key > prt.key:
                    self.left_rotate(prt)
                    tmp = prt
                    prt = node
                    node = tmp

                # if node is l_child
                gprt = prt.parent
                self.right_rotate(gprt)
                self.setBlack(gprt)
                self.setBlack(node)
                self.setRed(prt)
                node = prt
                continue
        
        self.setBlack(self.root)
