import random
from triple_dict_graph import TripleDictionaryGraph


class UI:
    def __init__(self):
        self.__graphs = list()
        self.__current_graph = None

    def add_empty_graph(self):
        if self.__current_graph is None:
            self.__current_graph = 0
        graph = TripleDictionaryGraph(0, 0)
        self.__graphs.append(graph)
        self.__current_graph = len(self.__graphs) - 1
        print("The empty graph has been successfully added !")

    @staticmethod
    def generate_random_graph(vertices, edges):
        if edges > vertices * vertices:
            raise ValueError("Too many edges!")
        graph = TripleDictionaryGraph(vertices, 0)
        i = 0
        while i < edges:
            x = random.randint(0, vertices - 1)
            y = random.randint(0, vertices - 1)
            cost = random.randint(0, 300)
            if graph.add_edge(x, y, cost):
                i += 1
        print("The graph has been successfully created !")
        return graph

    def ui_create_random_graph(self):
        try:
            vertices = int(input("Enter the number of vertices: "))
        except ValueError as ve:
            print(ve, "The number must be a positive integer!")
            return
        try:
            edges = int(input("Enter the number of edges: "))
        except ValueError as ve:
            print(ve, "The number must be a positive integer!")
            return
        graph = self.generate_random_graph(vertices, edges)
        if self.__current_graph is None:
            self.__current_graph = 0
        self.__graphs.append(graph)
        self.__current_graph = len(self.__graphs) - 1

    def ui_read_graph_from_file(self):
        filename = input("Enter the name of the file: ")
        if self.__current_graph is None:
            self.__current_graph = 0
        graph = TripleDictionaryGraph.read_from_file(filename)
        self.__graphs.append(graph)
        print("The graph has been succesfully added!")
        self.__current_graph = len(self.__graphs) - 1

    def ui_write_graph_to_file(self):
        current_graph = self.__graphs[self.__current_graph]
        output_file = "output" + str(self.__current_graph) + ".txt"
        TripleDictionaryGraph.write_graph_to_file(current_graph, output_file)

    def ui_switch_graph(self):
        print("You are on the graph number: {}".format(self.__current_graph))
        print("Available graphs: 0 - {}".format(str(len(self.__graphs) - 1)))
        number = int(input("Enter the graph number you want to switch to: "))
        if not 0 <= number < len(self.__graphs):
            raise ValueError("Trying to switch to a non existing graph!")
        self.__current_graph = number

    def ui_get_number_of_vertices(self):
        print("The number of vertices is: {}.".format(self.__graphs[self.__current_graph].get_number_of_vertices()))

    def ui_get_number_of_edges(self):
        print("The number of edges is: {}.".format(self.__graphs[self.__current_graph].get_number_of_edges()))

    def list_all_outbound(self):
        for vertex1 in self.__graphs[self.__current_graph].parse_set_vertices():
            line = str(vertex1) + " :"
            for vertex2 in self.__graphs[self.__current_graph].parse_outbound_vertices(vertex1):
                line = line + " " + str(vertex2)
            print(line)

    def list_outbound(self):
        vertex = int(input("Enter the vertex: "))
        line = str(vertex) + " :"
        for outbound_vertex in self.__graphs[self.__current_graph].parse_outbound_vertices(vertex):
            line = line + " " + "({}, {})".format(str(vertex), str(outbound_vertex))
        print(line)

    def list_all_inbound(self):
        for vertex1 in self.__graphs[self.__current_graph].parse_set_vertices():
            line = str(vertex1) + " :"
            for vertex2 in self.__graphs[self.__current_graph].parse_inbound_vertices(vertex1):
                line = line + " " + str(vertex2)
            print(line)

    def list_inbound(self):
        vertex = int(input("Enter the vertex: "))
        line = str(vertex) + " :"
        for inbound_vertex in self.__graphs[self.__current_graph].parse_inbound_vertices(vertex):
            line = line + " " + "({}, {})".format(str(inbound_vertex), str(vertex))
        print(line)

    def list_all_costs(self):
        for key in self.__graphs[self.__current_graph].parse_cost():
            line = "({}, {})".format(key[0], key[1]) + " :" + str(self.__graphs[self.__current_graph].cost_dictionary[key])
            print(line)

    def list_all_vertices(self):
        for vertex in self.__graphs[self.__current_graph].parse_set_vertices():
            print("{}".format(vertex))

    def ui_add_vertex(self):
        vertex = int(input("Enter the new vertex: "))
        added = self.__graphs[self.__current_graph].add_vertex(vertex)
        if added:
            print("Vertex added successfully!")
        else:
            print("Cannot add this vertex, it already exists!")

    def ui_remove_vertex(self):
        vertex = int(input("Enter the vertex to be deleted: "))
        deleted = self.__graphs[self.__current_graph].remove_vertex(vertex)
        if deleted:
            print("Vertex deleted successfully!")
        else:
            print("Cannot delete this vertex, it does not exist!")

    def ui_add_edge(self):
        print("Add an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        cost = int(input("Enter the cost of the edge: "))
        added = self.__graphs[self.__current_graph].add_edge(vertex_x, vertex_y, cost)
        if added:
            print("Edge added successfully!")
        else:
            print("Cannot add this edge, it already exists!")

    def ui_remove_edge(self):
        print("Remove an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        deleted = self.__graphs[self.__current_graph].remove_edge(vertex_x, vertex_y)
        if deleted:
            print("Edge deleted successfully!")
        else:
            print("Cannot remove this edge, it does not exist!")

    def ui_modify_cost(self):
        print("Modify the cost of an edge (an edge is (x, y))")
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        cost = int(input("Enter the cost of the edge: "))
        modified = self.__graphs[self.__current_graph].change_cost(vertex_x, vertex_y, cost)
        if modified:
            print("Cost modified successfully!")
        else:
            print("Cannot modify the cost, the edge does not exist!")

    def ui_get_in_degree(self):
        vertex = int(input("Enter the vertex:"))
        degree = self.__graphs[self.__current_graph].get_in_degree(vertex)
        if degree == -1:
            print("The vertex does not exist!")
        else:
            print("The in degree of the vertex {} is {}.".format(vertex, degree))

    def ui_get_out_degree(self):
        vertex = int(input("Enter the vertex:"))
        degree = self.__graphs[self.__current_graph].get_out_degree(vertex)
        if degree == -1:
            print("The vertex does not exist!")
        else:
            print("The out degree of the vertex {} is {}.".format(vertex, degree))

    def ui_check_edge(self):
        vertex_x = int(input("Enter x = "))
        vertex_y = int(input("Enter y = "))
        edge = self.__graphs[self.__current_graph].check_edge(vertex_x, vertex_y)
        if edge is not False:
            print("({}, {}) is an edge !".format(vertex_x, vertex_y))
        else:
            print("({}, {}) is not an edge!".format(vertex_x, vertex_y))

    def ui_copy_current_graph(self):
        copy = self.__graphs[self.__current_graph].copy_graph()
        self.__graphs.append(copy)
        print("The copy has been successfully created !4")

    def ui_BFS(self):
        start = int(input("Enter the start vertex: "))
        end = int(input("Enter the end vertex: "))
        path = self.__graphs[self.__current_graph].find_path_BFS(start, end)
        path_string = "The lowest length path is: "
        for vertex in path:
            path_string += f"{vertex}"
            path_string += " - "
        print(path_string[:-2])
        print(f"The length of the path is {len(path) - 1}")

    def low_cost_walk_ui(self):
        start = int(input("Enter the start vertex: "))
        end = int(input("Enter the end vertex:"))
        cost, walk = self.__graphs[self.__current_graph].lowest_cost_dp_matrix(start, end)
        print(f"The walk with the lowest cost from {start} to {end} is" + str(
            walk) + f" and has the cost {cost}")

    @staticmethod
    def print_menu():
        print("MENU:\n"
              "1. Create a random graph with specified number of vertices and edges.\n"
              "2. Read the graph from a text file.\n"
              "3. Write the graph in a text file.\n"
              "4. List all the vertices.\n"
              "5. List the number of vertices.\n"
              "6. List the number of edges.\n"
              "7. List the outbound edges of a given vertex.\n"
              "8. List all outbound vertices of the graph.\n"
              "9. List the inbound edges of a given vertex.\n"
              "10. List all inbound vertices of the graph. \n"
              "11. List the edges and their costs.\n"
              "12. Add a vertex.\n"
              "13. Remove a vertex.\n"
              "14. Add an edge.\n"
              "15. Remove an edge.\n"
              "16. Modify the cost of an edge.\n"
              "17. List the in degree of a vertex.\n"
              "18. List the out degree of a vertex.\n"
              "19. Check if there is an edge between two given vertices.\n"
              "20. Make a copy of the graph.\n"
              "21. Add an empty graph.\n"
              "22. Switch the graph.\n"
              "23. BFS\n"
              "x. EXIT.\n")

    def start(self):
        print("Welcome!")
        done = False
        self.add_empty_graph()
        print("The current graph is an empty graph!")
        command_dict = {"1": self.ui_create_random_graph, "2": self.ui_read_graph_from_file,
                        "3": self.ui_write_graph_to_file, "4": self.list_all_vertices,
                        "5": self.ui_get_number_of_vertices, "6": self.ui_get_number_of_edges,
                        "7": self.list_outbound, "8": self.list_all_outbound,
                        "9": self.list_inbound, "10": self.list_all_inbound,
                        "11": self.list_all_costs, "12": self.ui_add_vertex,
                        "13": self.ui_remove_vertex, "14": self.ui_add_edge,
                        "15": self.ui_remove_edge, "16": self.ui_modify_cost,
                        "17": self.ui_get_in_degree, "18": self.ui_get_out_degree,
                        "19": self.ui_check_edge, "20": self.ui_copy_current_graph,
                        "21": self.add_empty_graph, "22": self.ui_switch_graph,
                        "23": self.ui_BFS}
        while not done:
            try:
                self.print_menu()
                option = input("Choose an option from the menu: \n")
                if option == "x":
                    done = True
                    print("Good bye!")
                elif option in command_dict:
                    command_dict[option]()
                else:
                    print("The command does not exist!\n")
            except ValueError as ve:
                print(str(ve))
            except FileNotFoundError as fnfe:
                print(str(fnfe).strip("[Errno 2] "))



