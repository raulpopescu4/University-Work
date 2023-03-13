class AdjacencyMatrixGraph:
    def __init__(self, n):
        self.vertices = n
        self.graph = [[0 for i in range(n)] for j in range(n)]

    def is_edge(self, x, y):
        return y in self.graph[x]

    def add_edge(self, x, y, cost):
        if not self.is_edge(x, y):
            self.graph[x][y] = cost
            self.graph[y][x] = cost

    def prims_algorithm(self, starting_node):
        selected = [False] * self.vertices
        no_edge = 0
        selected[starting_node] = True
        print("  Edge  : Weight")
        while no_edge < self.vertices - 1:
            minimum = 100000000
            source_node = 0
            destination_node = 0
            for i in range(len(selected)):
                if selected[i]:
                    for j in range(len(selected)):
                        if not(selected[j]) and self.graph[i][j]:
                            if minimum > self.graph[i][j]:
                                minimum = self.graph[i][j]
                                source_node = i
                                destination_node = j
            print(f"{source_node} +  -   + {destination_node} +   :   + {self.graph[source_node][destination_node]}")
            selected[destination_node] = True
            no_edge += 1


class MainProgram:
    def __init__(self):
        file = open("input.txt", "r")
        number_of_vertices, number_of_edges = map(int, file.readline().split())
        self.g = AdjacencyMatrixGraph(int(number_of_vertices))

        for edge in range(number_of_edges):
            x, y, cost = map(int, file.readline().split())
            self.g.add_edge(x, y, cost)

    def run(self):
        x = input("Choose the starting node: ")
        x = int(x)
        self.g.prims_algorithm(x)


program = MainProgram()
program.run()