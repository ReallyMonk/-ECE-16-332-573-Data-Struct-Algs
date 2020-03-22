import random
from RB_tree import RB_tree
from LLRB_tree import LLRB_tree


def create_tree(keys):
    new_tree = LLRB_tree()
    for i in keys:
        new_tree.insert(i)
    return new_tree


for i in [4, 5, 6]:
    print(i)
    keys = list(range(10**i))

    res_100 = []
    timer = 1
    while timer > 0:
        random.shuffle(keys)
        tree = create_tree(keys)
        print(tree.red_node)
        timer = timer - 1
    #res.append(res_100)

#print(sum(res[0]) / len(res[0]))
#print(sum(res[1]) / len(res[1]))
#print(sum(res[2]) / len(res[2]))

#print('res', cnt_red(create_tree(keys)))
