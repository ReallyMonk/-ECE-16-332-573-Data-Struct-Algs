from read_file import read

VERTIX_NUM = 8
#EDGES_NUM = 15
INF = float('inf')

data_A = read(
    'F:\Rutgers\\2ndSemester\DATA STRUCT & ALGS\Homework\hwk4\Q6\\a.txt')
data_B = read(
    'F:\Rutgers\\2ndSemester\DATA STRUCT & ALGS\Homework\hwk4\Q6\\b.txt')


class graph():
    def __init__(self, data):
        self.data = sorted(data, key=lambda x: x[2])
        self.disTo = [INF for i in range(VERTIX_NUM)]
        self.edgeTo = [None for i in range(VERTIX_NUM)]
        self.vertix = [False for i in range(VERTIX_NUM)]

    def normal_dij(self, ver=0):
        # initialize the disTo array
        self.disTo[ver] = 0
        self.vertix[ver] = True
        for edge in self.data:
            if edge[0] == ver:
                self.disTo[edge[1]] = edge[2]
                self.edgeTo[edge[1]] = edge
        print('initial--------')
        print(self.disTo)
        print('----------------')

        # start relax
        while False in self.vertix:
            # find the cloest node
            index = []
            for i in range(len(self.vertix)):
                if not self.vertix[i]:
                    index.append(i)

            cur_node = index[0]
            for node in index:
                if self.disTo[node] < self.disTo[cur_node]:
                    cur_node = node

            # set cur_node beening fixed
            self.vertix[cur_node] = True
            print('node ', cur_node)
            # update edge according to cur_node
            for edge in self.data:
                print('viewing', edge)
                if edge[0] == cur_node:
                    new_len = edge[2] + self.disTo[edge[0]]
                    print(new_len)
                    if self.disTo[edge[1]] > new_len:
                        self.disTo[edge[1]] = new_len
                        self.edgeTo[edge[1]] = edge
                    else:
                        pass

            print(self.disTo)
            print(self.edgeTo)
            print(self.vertix)
            print('-----------------')


test_data = [[0, 2, 10], [0, 4, 30], [0, 5, 100], [1, 2, 5], [2, 3, 50],
             [4, 3, 20], [4, 5, 60], [3, 5, 10]]
test_data = [[0, 3, 2], [0, 1, 4], [1, 2, 6], [2, 3, -9]]
t = graph(data_B)
t.normal_dij()
print(t.vertix)
print(t.disTo)
print(t.edgeTo)
