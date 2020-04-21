from read_file import read

VERTIX_NUM = 264346
EDGES_NUM = 733846
data = read(
    "F:\Rutgers\\2nd Semester\DATA STRUCT & ALGS\Homework\hwk4\Q5\\NYC.txt")

#data = [[1, 2], [2, 3], [1, 3], [1, 6], [4, 6], [4, 5], [3, 4], [3, 5]]


class graph():
    def __init__(self):
        self.graph = self.create_graph()
        self.trace = [False for i in range(VERTIX_NUM)]

    def create_graph(self):
        graph = [[] for i in range(VERTIX_NUM)]

        for edge in data:
            graph[edge[0]-1].append(edge[1])
            graph[edge[1]-1].append(edge[0])

        return graph

    def dfs(self, ver):
        print('check ', ver)
        self.trace[ver-1] = True

        for child_ver in self.graph[ver-1]:
            if not self.trace[child_ver-1]:
                self.dfs(child_ver)

        print(ver, 'done')
        return

    def bfs(self, ver):
        queue = [ver]

        while queue:
            print(queue)
            #print(self.trace)
            self.trace[ver-1] = True

            for child in self.graph[ver-1]:
                if not self.trace[child-1] and child not in queue:
                    queue.append(child)
            
            del(queue[0])
            if queue:
                ver = queue[0]


dfs_g = graph()
print(dfs_g.graph)
dfs_g.dfs(1)
print(dfs_g.trace)


bfs_g = graph()
print(bfs_g.graph)
bfs_g.bfs(1)
