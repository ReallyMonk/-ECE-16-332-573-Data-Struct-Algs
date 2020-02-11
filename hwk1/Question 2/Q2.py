import time
import os


class QF:
    def __init__(self):
        self.id = [i for i in range(0, 8193)]

    def Union(self, pair):
        pid = self.id[pair[0]]
        qid = self.id[pair[1]]
        for i in range(0, 8193):
            if pid == self.id[i]:
                self.id[i] = qid

    def connected(self, pair):
        return self.id[pair[0]] == self.id[pair[1]]

    def exe(self, pair):
        if not self.connected(pair):
            self.Union(pair)


class QU:
    def __init__(self):
        self.id = [i for i in range(0, 8193)]

    def root(self, i):
        while i != self.id[i]:
            i = self.id[i]
        return i

    def Union(self, pair):
        p = self.root(pair[0])
        q = self.root(pair[1])
        self.id[p] = q

    def connected(self, pair):
        return self.root(pair[0]) == self.root(pair[1])

    def exe(self, pair):
        if not self.connected(pair):
            self.Union(pair)


class WQU:
    def __init__(self):
        self.sz = [1 for i in range(0, 8193)]
        self.id = [i for i in range(0, 8193)]

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def Union(self, pair):
        p = self.root(pair[0])
        q = self.root(pair[1])
        if self.sz[p] < self.sz[q]:
            self.id[p] = q
            self.sz[q] = self.sz[p] + self.sz[q]
        else:
            self.id[q] = p
            self.sz[p] = self.sz[q] + self.sz[p]

    def connected(self, pair):
        return self.root(pair[0]) == self.root(pair[1])

    def exe(self, pair):
        if not self.connected(pair):
            self.Union(pair)

# input the address of your dataset
path = 'D:\Rutgers/2nd Semester\DATA STRUCT & ALGS\Homework\hwk1\Question 2\hw1-2.data'
files = os.listdir(path)

# initial

for file in files:
    f = open(path + '/' + file)
    iter_f = iter(f)
    num_pairs = []

    # read digit from files and save them into a list
    for num in iter_f:
        strs = num.split(' ')
        num_p = [int(strs[0]), int(strs[1])]
        num_pairs.append(num_p)

    print(file)
    # initial classes
    QFtest = QF()
    QUtest = QU()
    WQUtest = WQU()
    '''
    for num_pair1 in num_pairs:
        QFtest.exe(num_pair1)
    for num_pair1 in num_pairs:
        QFtest.exe(num_pair1)
    for num_pair1 in num_pairs:
        QFtest.exe(num_pair1)
'''
    # time counting for union process
    start = time.perf_counter()

    for num_pair1 in num_pairs:
        QFtest.exe(num_pair1)
    time1 = time.perf_counter()

    for num_pair1 in num_pairs:
        QFtest.exe(num_pair1)
    time2 = time.perf_counter()

    for num_pair1 in num_pairs:
        QFtest.exe(num_pair1)
    time3 = time.perf_counter()

    last_time1 = time1 - start
    last_time2 = time2 - time1
    last_time3 = time3 - time2

    wpath = 'D:\Rutgers/2nd Semester\DATA STRUCT & ALGS\Homework\hwk1\Question 2/res'
    f1 = open(wpath + '/Ftime1.txt', 'a')
    f1.write(str(last_time1) + '\n')
    f1.close()
    f2 = open(wpath + '/Ftime2.txt', 'a')
    f2.write(str(last_time2) + '\n')
    f2.close()
    f3 = open(wpath + '/Ftime3.txt', 'a')
    f3.write(str(last_time3) + '\n')
    f3.close()

    print('end')
'''
f = open(path + '/512pair.txt')
iter_f = iter(f)
num_pairs = []

for num in iter_f:
    strs = num.split(' ')
    num_p = [int(strs[0]), int(strs[1])]
    num_pairs.append(num_p)

QFtest = QF()
QUtest = QU()
WQUtest = WQU()

i = 0
for num_p in num_pairs:
    i = i + 1
    print(i)
    WQUtest.Union(num_p)

print(WQUtest.connected(num_pairs[0]))
'''