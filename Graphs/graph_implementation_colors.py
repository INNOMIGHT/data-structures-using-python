from collections import OrderedDict
from enum import Enum


class State(Enum):
    unvisited = 1  # white
    visited = 2  # black
    visiting = 3  # gray


class Node:

    def __init__(self, num):
        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict()  # key = node, val = weight

    def __str__(self):
        return self.num


class Graph:

    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, num):
        self.nodes[num] = Node(num)

    def add_edge(self, curr, dest, weight):
        if curr not in self.nodes:
            self.add_node(curr)
        if dest not in self.nodes:
            self.add_node(dest)

        self.nodes[curr].adjacent[self.nodes[dest]] = weight


g = Graph()
g.add_edge(1, 2, 4)

print(g.nodes)
