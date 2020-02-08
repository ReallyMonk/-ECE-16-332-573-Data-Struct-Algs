import time
import os


class QF:
    def Union(self, pair):
        pid = id[pair[0]]
        qid = id[pair[1]]
        for i in range(0, 8193):
            if pid == id[i]:
                id[i] = qid

    def connected(self, pair):
        return pair[0] == pair[1]


class QU:
    def root(self, i):
        while i != id[i]:
            i = id[i]
        return i

    def Union(self, pair):
        p = pair[0]
        q = pair[1]
        id[p] = q

    def connected(self, pair):
        return self.root(pair[0]) == self.root(pair[1])


class WQU:
    def __init__(self):
        self.sz = [1 for i in range(0, 8193)]

    def root(self, i):
        while i != id[i]:
            i = id[i]
        return i

    def Union(self, pair):
        p = self.root(pair[0])
        q = self.root(pair[1])
        if self.sz[p] < self.sz[q]:
            id[p] = q
            self.sz[p] = self.sz[p] + self.sz[q]
        else:
            id[q] = p
            self.sz[q] = self.sz[q] + self.sz[p]

    def connected(self, pair):
        return self.root(pair[0]) == self.root(pair[1])


path = './hw1-2.data'
files = os.listdir(path)

# initial
id = [i for i in range(0, 8193)]

for file in files:
    f = open(path + '/' + file)
    iter_f = iter(f)
    num_pairs = []

    # read digit from files and save them into a list
    for num in iter_f:
        strs = num.split(' ')
        num_p = [int(strs[0]), int(strs[1])]
        num_pairs.append(num_p)

    # initial classes
    QFtest = QF()
    QUtest = QU()
    WQUtest = WQU()
    # time counting for reading sequence
    start = time.clock()
    #for num_pair1 in num_pairs:
    #    QFtest.Union(num_pair1)
    time1 = time.clock()
    #for num_pair2 in num_pairs:
    #    QUtest.Union(num_pair2)
    time2 = time.clock()
    #for num_pair3 in num_pairs:
    #    WQUtest.Union(num_pair3)
    time3 = time.clock()

    last_time1 = time1 - start
    last_time2 = time2 - time1
    last_time3 = time3 - time2
