class Vertex:

    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_nbr(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to[nbr]

    def __str__(self):
        return str(self.id) + "connected to " + str([x.id for x in self.connected_to])


class Graph:

    def __init__(self):
        self.vert_list = {}
        self.num_vert = 0

    def add_vertex(self, key):
        self.num_vert += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, v):
        if v not in self.vert_list:
            return None
        else:
            return self.vert_list[v]

    def add_edge(self, from_vert, to_vert, cost=0):
        if from_vert not in self.vert_list:
            nv = self.add_vertex(from_vert)
        if to_vert not in self.vert_list:
            nv = self.add_vertex(to_vert)
        self.vert_list[from_vert].add_nbr(self.vert_list[to_vert], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def __contains__(self, item):
        return item in self.vert_list


graph_one = Graph()
for i in range(6):
    graph_one.add_vertex(i)

graph_one.add_edge(0, 1, 2)

for vertex in graph_one:
    print(vertex)
    print(vertex.get_connections())







