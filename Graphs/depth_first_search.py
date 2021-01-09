graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        visit = stack.pop()
        print(visit)
        if visit not in visited:
            visited.add(visit)
            stack.extend(graph[visit] - visited)
            print(stack)

    return visited


print(dfs(graph, 'A'))
