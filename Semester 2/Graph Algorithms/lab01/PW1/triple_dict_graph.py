import copy
import math


class TripleDictionaryGraph:
    def __init__(self, number_of_vertices, number_of_edges):
        self.number_of_vertices = number_of_vertices
        self.number_of_edges = number_of_edges
        self.inbound_dictionary = dict()
        self.outbound_dictionary = dict()
        self.cost_dictionary = dict()
        for index in range(number_of_vertices):
            self.inbound_dictionary[index] = list()
            self.outbound_dictionary[index] = list()

    def get_number_of_edges(self):
        return self.number_of_edges

    def get_number_of_vertices(self):
        return self.number_of_vertices

    def parse_set_vertices(self):
        vertices = list(self.inbound_dictionary.keys())
        for vertex in vertices:
            yield vertex

    def check_edge(self, vertex1, vertex2):
        edge = (vertex1, vertex2)
        if vertex1 in self.inbound_dictionary[vertex2]:
            return edge
        elif vertex2 in self.outbound_dictionary[vertex1]:
            return edge
        return False

    def get_in_degree(self, vertex):
        if vertex not in self.inbound_dictionary.keys():
            return -1
        return len(self.inbound_dictionary[vertex])

    def get_out_degree(self, vertex):
        if vertex not in self.outbound_dictionary.keys():
            return -1
        return len(self.outbound_dictionary[vertex])

    def parse_outbound_vertices(self, vertex):
        for outbound_vertex in self.outbound_dictionary[vertex]:
            yield outbound_vertex

    def parse_inbound_vertices(self, vertex):
        for inbound_vertex in self.inbound_dictionary[vertex]:
            yield inbound_vertex

    def change_cost(self, edge_x, edge_y, cost):
        if (edge_x, edge_y) not in self.cost_dictionary.keys():
            return False
        self.cost_dictionary[(edge_x, edge_y)] = cost
        return True

    def add_vertex(self, vertex):
        if vertex in self.inbound_dictionary.keys() and vertex in self.outbound_dictionary.keys():
            return False
        self.inbound_dictionary[vertex] = list()
        self.outbound_dictionary[vertex] = list()
        self.number_of_vertices += 1
        return True

    def add_edge(self, vertex1, vertex2, cost):
        if vertex1 in self.inbound_dictionary[vertex2]:
            return False
        elif vertex2 in self.outbound_dictionary[vertex1]:
            return False
        elif (vertex1, vertex2) in self.cost_dictionary.keys():
            return False
        self.number_of_edges += 1
        self.inbound_dictionary[vertex1].append(vertex2)
        self.outbound_dictionary[vertex2].append(vertex1)
        self.cost_dictionary[(vertex1, vertex2)] = cost
        return True

    def remove_edge(self, vertex1, vertex2):
        # if vertex1 not in self.inbound_dictionary.keys() or vertex2 not in self.inbound_dictionary.keys():
        #     return False
        # if vertex1 not in self.outbound_dictionary.keys() or vertex2 not in self.outbound_dictionary.keys():
        #     return False
        # if vertex2 not in self.inbound_dictionary[vertex1]:
        #     return False
        # if vertex1 not in self.outbound_dictionary[vertex2]:
        #     return False
        if vertex1 not in self.inbound_dictionary.keys() or vertex2 not in self.inbound_dictionary.keys() or vertex1 not in self.outbound_dictionary.keys() or vertex2 not in self.outbound_dictionary.keys():
            return False
        if vertex1 not in self.inbound_dictionary[vertex2]:
            return False
        elif vertex2 not in self.outbound_dictionary[vertex1]:
            return False
        elif (vertex1, vertex2) not in self.cost_dictionary.keys():
            return False
        self.number_of_edges -= 1
        self.inbound_dictionary[vertex1].remove(vertex2)
        self.outbound_dictionary[vertex2].remove(vertex1)
        self.cost_dictionary.pop((vertex1, vertex2))
        return True

    def remove_vertex(self, vertex):
        if vertex not in self.inbound_dictionary.keys() or vertex not in self.outbound_dictionary.keys():
            return False
        self.inbound_dictionary.pop(vertex)
        self.outbound_dictionary.pop(vertex)
        for key in self.inbound_dictionary.keys():
            if vertex in self.inbound_dictionary[key]:
                self.inbound_dictionary[key].remove(vertex)
            elif vertex in self.outbound_dictionary[key].remove(vertex):
                self.outbound_dictionary[key].remove(vertex)
        cost_dictionary_list = list(self.cost_dictionary.keys())
        for key in cost_dictionary_list:
            if key[0] == vertex or key[1] == vertex:
                self.cost_dictionary.pop(key)
                self.number_of_edges -= 1
        self.number_of_vertices -= 1

        return True

    def parse_cost(self):
        edges = list(self.cost_dictionary.keys())
        for edge in edges:
            yield edge

    def copy_graph(self):
        return copy.deepcopy(self)

    @staticmethod
    def read_from_file(filename):
        file = open(filename, "r")
        line = file.readline()
        line = line.strip()
        vertices, edges = line.split(' ')
        graph = TripleDictionaryGraph(int(vertices), int(edges))
        line = file.readline().strip()
        while len(line) > 0:
            line = line.split(' ')
            if len(line) == 1:
                graph.inbound_dictionary[int(line[0])] = []
                graph.outbound_dictionary[int(line[0])] = []
            else:
                graph.inbound_dictionary[int(line[1])].append(int(line[0]))
                graph.outbound_dictionary[int(line[0])].append(int(line[1]))
                graph.cost_dictionary[(int(line[0]), int(line[1]))] = int(line[2])
            line = file.readline().strip()
        file.close()
        return graph

    @staticmethod
    def write_graph_to_file(graph, file):
        file = open(file, "w")
        first_line = str(graph.number_of_vertices) + ' ' + str(graph.number_of_edges) + '\n'
        file.write(first_line)
        if len(graph.cost_dictionary) == 0 and len(graph.inbound_dictionary) == 0:
            raise ValueError("There is nothing that can be written!")
        for edge in graph.cost_dictionary.keys():
            new_line = "{} {} {}\n".format(edge[0], edge[1], graph.cost_dictionary[edge])
            file.write(new_line)
        for vertex in graph.inbound_dictionary.keys():
            if len(graph.inbound_dictionary[vertex]) == 0 and len(graph.outbound_dictionary[vertex]) == 0:
                new_line = "{}\n".format(vertex)
                file.write(new_line)
        print("The graph has been successfully written !")
        file.close()

    def find_path_BFS(self, start, end):
        # I check the input
        if start not in self.inbound_dictionary.keys() and start not in self.outbound_dictionary.keys():
            raise ValueError("invalid start")
        if end not in self.inbound_dictionary.keys() and start not in self.outbound_dictionary.keys():
            raise ValueError("invalid end")
        # I use visited for the visited nodes to avoid loops
        visited = []
        # I use queue to remember all the paths, considering it as a queue data container
        queue = [[start]]
        # if the start vertex is equal to the end vertex I return an empty path and length -1
        if start == end:
            return []
        # while there are paths unchecked
        while queue:
            path = queue.pop(0)
            # vertex is the last vertex from the path
            vertex = path[-1]
            # if the vertex is not visited, for each of its outbound vertex, I create a new path from the
            # previous one by adding the outbound vertex. If the outbound vertex coincides with the end vertex
            # I return the path created
            if vertex not in visited:
                outbound_vertices = self.outbound_dictionary[vertex]
                for outbound_vertex in outbound_vertices:
                    new_path = list(path)
                    new_path.append(outbound_vertex)
                    queue.append(new_path)
                    if outbound_vertex == end:
                        return new_path
                visited.append(vertex)
                # if it wasn't the end I add it to the list of visited vertices
        # if I never reach the end it means there is no path
        raise ValueError("No path between start and end")

    def lowest_cost_dp_matrix(self, start, end):
        inf = math.inf
        dist = [[inf for _ in range(self.number_of_vertices)] for _ in range(self.number_of_vertices)]
        parent = [[0 for _ in range(self.number_of_vertices)] for _ in range(self.number_of_vertices)]
        dist[start][0] = 0
        for i in range(1, self.number_of_vertices):
            for v in range(self.number_of_vertices):
                minimum = dist[v][i - 1]
                parent[v][i] = v
                for u in self.inbound_dictionary[v]:
                    if dist[u][i - 1] + self.cost_dictionary[(u, v)] < minimum:
                        minimum = dist[u][i - 1] + self.cost_dictionary[(u, v)]
                        parent[v][i] = u

                dist[v][i] = minimum

        return dist[end][self.number_of_vertices - 1], self.build_path_dp(parent, end)

    def build_path_dp(self, parent, end):
        t = end
        c = self.number_of_vertices - 1
        path = []

        while c > 0:
            if parent[t][c] != parent[t][c - 1]:
                path.insert(0, parent[t][c])
                t = parent[t][c]
            c = c - 1

        return path
