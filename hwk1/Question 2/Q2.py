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
        if pair[0] == pair[1]:
            return True
        else:
            return False


class QU:
    def root(self, i):
        while i != id[i]:
            i = id[i]
        return i

    def Union(self, pair):
        p = pair[0]
        q = pair[1]
        id[p] = q


class WQU:
    def root(self, i):
        while i != id[i]:
            id[i] = id[id[i]]
            i = id[i]
        return i

    def Union(self, pair):
        p = pair[0]
        q = pair[1]
        id[p] = q

path = 'D:/Rutgers/2nd Semester/DATA STRUCT & ALGS/Homework/hwk1/Question 2/hw1-2.data'
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
    # time counting
    start = time.clock()
    #for num_pair1 in num_pairs:
    #    QFtest.Union(num_pair1)
    time1 = time.clock()
    for num_pair2 in num_pairs:
        QUtest.Union(num_pair2)
    time2 = time.clock()
    for num_pair3 in num_pairs:
        WQUtest.Union(num_pair3)
    time3 = time.clock()

    last_time1 = time1 - start
    last_time2 = time2 - time1
    last_time3 = time3 - time2

    print(last_time3)