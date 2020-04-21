from read_file import read
import time


class graph():
    def __init__(self, data):
        # sort the data by weights
        self.data = sorted(data, key=(lambda x: x[2]))
        self.total_nodes = self.find_max_vertice() + 1
        self.forest = [i for i in range(self.total_nodes)]
        self.vertices = []

    def find_max_vertice(self):
        dt = self.data
        max = dt[0][0]
        for vt in dt:
            if vt[0] > vt[1]:
                if max < vt[0]:
                    max = vt[0]
            else:
                if max < vt[1]:
                    max = vt[1]
        return max

    def check_id(self, ver):
        while self.forest[ver] != ver:
            ver = self.forest[ver]
        return ver

    def connect(self, root, node):
        #print('connect ', node, 'to ', root)
        self.forest[self.check_id(node)] = self.check_id(root)

    def kruskal(self):
        total_weight = 0
        total_edge = 0
        for vertice in self.data:
            # check if the two vetice are in the same tree
            # if not, connect them and accumulate weight
            #print('check', vertice)
            if self.check_id(vertice[0]) != self.check_id(vertice[1]):
                self.connect(vertice[0], vertice[1])
                total_weight = total_weight + vertice[2]
                total_edge = total_edge + 1
                #print(total_edge)

            if total_edge == self.total_nodes - 1:
                return total_weight

        return total_weight

    def prime(self):
        # initial
        self.vertices.append(0)
        total_weights = 0

        while len(self.vertices) < self.total_nodes:
            #print(self.vertices)
            for edge in self.data:
                if edge[0] in self.vertices:
                    if edge[1] in self.vertices:
                        continue
                    else:
                        self.vertices.append(edge[1])
                        total_weights = total_weights + edge[2]
                        break
                else:
                    if edge[1] in self.vertices:
                        self.vertices.append(edge[0])
                        total_weights = total_weights + edge[2]
                        break
                    else:
                        continue

        return total_weights


path = 'F:\Rutgers\\2nd Semester\DATA STRUCT & ALGS\Homework\hwk4\Q2\\data.txt'
data = read(path)
#print(data)
'''
data = [[0, 1, 1], [0, 4, 2], [3, 4, 1], [2, 3, 1], [0, 3, 1], [4, 6, 3],
        [6, 5, 1], [4, 5, 1], [5, 7, 1], [9, 2, 1], [10, 2, 1], [10, 9, 2],
        [7, 8, 1], [10, 8, 3]]
'''
gph_p = graph(data)
#print(gph_p.total_nodes)

t0 = time.time()
#print(gph_p.vertices)
print('prime weight', gph_p.prime())
#print(gph_p.vertices.sort())
t1 = time.time()


gph_k = graph(data)
#print(gph_k.data)
#print(gph_k.forest)
t2 = time.time()
print('kruskal weight', gph_k.kruskal())
#print(gph_k.forest)
t3 = time.time()

print('prime ', t1-t0)
print('kruskal ', t3-t2)