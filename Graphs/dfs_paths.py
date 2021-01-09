graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs_paths(g, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        print((vertex, path))
        for nxt in g[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))


print(list(dfs_paths(graph, 'A', 'F')))
