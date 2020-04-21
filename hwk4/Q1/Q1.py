from read_file import read


class graph():
    def __init__(self, data):
        self.graph = None
        self.data = data
        self.track = []
        #self.cur_vertice = None

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

    def create_graph(self):
        vertice_num = self.find_max_vertice()
        graph = [[] for i in range(vertice_num + 1)]
        #print(len(graph))

        for edge in self.data:
            #print(edge)
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        self.graph = graph
        return self.graph

    def dfs(self, ver, last):
        if not self.track:
            self.track = [None for i in range(len(self.graph))]

        self.track[ver] = True
        #print('current view ', ver)
        #print(self.track)

        # if ther is a cycle
        for vert in self.graph[ver]:
            if vert != last:
                #print('next ', vert)
                if not self.track[vert]:
                    self.dfs(vert, ver)
                else:
                    return False

        #print(ver, ' done')
        return True


path = 'F:\Rutgers\\2nd Semester\DATA STRUCT & ALGS\Homework\hwk4\Q1\\data.txt'
data = read(path)
#data = [[0, 1], [0, 4], [3, 4], [2, 3], [0, 3]]

new_graph = graph(data)
graph = new_graph.create_graph()
print(graph)
res = new_graph.dfs(0, None)
print(res)
