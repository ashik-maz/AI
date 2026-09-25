from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

graph = {}

# Edge input
e = int(input("Number of edges: "))

for i in range(e):
    u, v = input("Edge: ").split()

    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)      # bidirectional


def bfs(start, goal):
    q = deque([(start, [start])])
    visited = set()

    while q:
        node, path = q.popleft()

        print("Expand:", node)
        print("Queue:", list(q))

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for child in graph[node]:
                if child not in visited:
                    q.append((child, path + [child]))


start = input("Start: ")
goal = input("Goal: ")

path = bfs(start, goal)

print("BFS Path:", path)


# Draw graph
G = nx.Graph()

for node in graph:
    for child in graph[node]:
        G.add_edge(node, child)

pos = nx.spring_layout(G, seed=1)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=1500
)

plt.title("BFS Graph")
plt.show()