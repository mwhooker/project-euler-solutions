from uuid import uuid4
import networkx as nx

# read the file
f = open('67_triangle.txt')
graph = list()
for line in f:
    graph.append(line.split(' '))

# build the node list
root = None
nodes = dict()
lookup = dict()
for row in xrange(len(graph)):
    for col in xrange(len(graph[row])):
        node_key = (row, col)
        nodes[node_key] = uuid4()
        lookup[nodes[node_key]] = graph[row][col]
        if row is 0 and col is 0:
            root = nodes[node_key]

# build the graph
G = nx.DiGraph()
terminals = set()
for i in nodes:
    y,x = i
    if y+1 >= len(graph):
        terminals.add(nodes[i])
        continue
    G.add_edge(nodes[i], nodes[(y+1,x)], weight=(100-int(graph[y+1][x])))
    G.add_edge(nodes[i], nodes[(y+1, x+1)], weight=(100-int(graph[y+1][x+1])))

# find the shortest paths
paths = dict()
for t in terminals:
    # TODO: change length to N time using lookup dict
    len = nx.shortest_path_length(G, source=root, target=t, weighted=True)
    path =nx.shortest_path(G, source=root, target=t, weighted=True)
    paths[len] = path

# which is the shortest shortest path?
best = min(paths)
t = 0
for i in paths[best]:
    t += int(lookup[i])
print t
