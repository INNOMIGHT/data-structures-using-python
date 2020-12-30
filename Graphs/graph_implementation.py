class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def add_neighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def get_weight(self, nbr):
        return self.connectedTo[nbr]

    def get_connections(self):
        return self.connectedTo.keys()

    def get_id(self):
        return self.id

    def __str__(self):
        return str(self.id) + " connected to " + str([x.id for x in self.connectedTo])


class Graph:

    def __init__(self):
        self.vert_list = {}
        self.num_vertices = 0

    def add_vertex(self, key):
        new_vert = Vertex(key)
        self.vert_list[key] = new_vert
        self.num_vertices += 1
        return new_vert

    def add_edge(self, f, t, cost=0):
        if f not in self.vert_list:
            nv = self.add_vertex(f)
        if t not in self.vert_list:
            nv = self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())

    def __contains__(self, item):
        return for item in self.vert_list


g_one = Graph()
for i in range(1, 6):
    g_one.add_vertex(i)

for items in g_one:
    print(items)