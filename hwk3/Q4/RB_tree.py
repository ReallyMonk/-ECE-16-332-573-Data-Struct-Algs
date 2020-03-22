# a balanced red black tree
class RB_node():
    def __init__(self, key, color=False):
        self.key = key
        self.color = color  # Red = False, Black = True
        self.l_child = None
        self.r_child = None
        self.parent = None


class RB_tree():
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

        # prt exist and is red
        while self.isRed(node.parent):
            prt = node.parent
            gprt = node.parent

            # prt is left child of prt
            if prt == gprt.l_child:
                # case 1 if uncle is red
                uncle = gprt.r_child
                if self.isRed(uncle):
                    self.setBlack(uncle)
                    self.setBlack(prt)
                    self.setRed(gprt)
                    node = gprt
                    continue
                
                # case 2 if uncle is black and node is r_child
                # change this situation to case 3
                if node.key > prt.key:
                    self.left_rotate(prt)
                    tmp = prt
                    prt = node
                    node = tmp
                
                # case 3 node is left child
                self.setBlack(prt)
                self.setRed(gprt)
                self.right_rotate(gprt)
            
            # prt is right child to gprt
            else:
                # case 1 uncle is red
                uncle = gprt.l_child
                if self.isRed(uncle):
                    self.setBlack(uncle)
                    self.setBlack(prt)
                    self.setRed(gprt)
                    node = gprt
                    continue
                
                # case 2 uncle is black and node is l_child
                if node.key < prt.key:
                    self.right_rotate(prt)
                    tmp = prt
                    prt = node
                    node = tmp
                
                # case 3 node is r_child
                self.setBlack(prt)
                self.setRed(gprt)
                self.left_rotate(gprt)
        
        self.setBlack(self.root)
                

keys = [9, 6, 4, 3, 0, 7, 1, 5, 8, 2]

tree = RB_tree()
for key in keys:
    tree.insert(key)

print(tree.red_node)