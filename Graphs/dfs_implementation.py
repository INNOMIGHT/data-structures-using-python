adj_list = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['B', 'F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

color = {}
parent = {}
trav_time = {}
dfs_trav_output = []

# initialize
for node in adj_list.keys():
    color[node] = 'W'
    parent[node]: None
    trav_time[node] = [-1, -1]

time = 0


# dfs_algo
def dfs_algo(u):
    global time
    color[u] = 'G'
    trav_time[u][0] = time
    dfs_trav_output.append(u)
    time += 1

    for v in adj_list[u]:
        if color[v] == 'W':
            parent[v] = u
            dfs_algo(v)

    color[u] = 'B'
    trav_time[u][1] = time
    time += 1

    for u in adj_list.keys():
        if color[u] == 'W':
            dfs_algo(u)

dfs_algo('A')
print(dfs_trav_output)
print(trav_time)

