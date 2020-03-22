from LLRB_tree import LLRB_tree
import random


# create tree
def create_tree(N):
    tree = LLRB_tree()
    keys = list(range(N))
    random.shuffle(keys)

    for k in keys:
        tree.insert(k)

    return tree


# find a random node
def find_node(key, node):
    if key < node.key and node.l_child:
        return find_node(key, node.l_child) + 1
    elif key > node.key and node.r_child:
        return find_node(key, node.r_child) + 1
    else:
        return 1


def find_path(N):
    # ran_key = random.randint(0, N)
    tree = create_tree(N)
    paths = []
    for ran_key in range(N):
        paths.append(find_node(ran_key, tree.root))

    avg = sum(paths) / N

    cov = 0
    for s in paths:
        cov = cov + (s - avg)**2

    std = (cov / N)**0.5

    return avg, std


res = []
for i in range(0, 10001, 500):
    if i == 0:
        continue
    print(i)
    cnt_down = 1000

    avg_res = []
    std_res = []
    while cnt_down > 0:
        cnt_down = cnt_down - 1
        avg, std = find_path(i)
        avg_res.append(avg)
        std_res.append(std)

    print(sum(avg_res) / len(avg_res))
    print(sum(std_res) / len(std_res))
