"""


75(95(17,47),64(47,82))
75 (0,0) 1
95 (1,0) 2
64 (1,1) 3
17 (2,0) 4
47 (2,1) 5
82 (2,2) 6
18 (3,0)
35 (3,1)
87 (3,2)
10 (3,3)

(0,0) (1,0)
(0,0) (1,1)
(1,0) (2,0)
(1,0) (2,1)
(1,1) (2,1)
(1,1) (2,2)
(2,0) (3,0)
(2,0) (3,1)
(2,1) (3,1)
(2,1) (3,2)
(2,2) (3,2)
(2,2) (3,3)

75 95
75 64
95 17
95 47
64 47
64 82

75
95 64
17 47 82
"""

from uuid import uuid4
from pprint import pprint
import networkx as nx

G = nx.DiGraph()
f = open('triangle')
graph = list()
for line in f:
    graph.append(line.split(' '))

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

terminals = set()
for i in nodes:
    y,x = i
    if y+1 >= len(graph):
        terminals.add(nodes[i])
        continue
    G.add_edge(nodes[i], nodes[(y+1,x)], weight=(100-int(graph[y+1][x])))
    G.add_edge(nodes[i], nodes[(y+1, x+1)], weight=(100-int(graph[y+1][x+1])))

paths = dict()
for t in terminals:
    len = nx.shortest_path_length(G, source=root, target=t, weighted=True)
    path =nx.shortest_path(G, source=root, target=t, weighted=True)
    paths[len] = path

best = min(paths)
t = 0
for i in paths[best]:
    t += int(lookup[i])
print t
