import heapq
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


# Heuristic input
h = {}

print("Enter heuristic values:")

for node in graph:
    h[node] = int(input("h(" + node + "): "))


start = input("Start: ")
goal = input("Goal: ")


def greedy(start, goal):

    pq = [(h[start], start, [start])]
    visited = set()

    while pq:

        hv, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        print("Expand:", node, "h =", hv)

        if node == goal:
            return path

        for child in graph[node]:

            if child not in visited:
                heapq.heappush(
                    pq, (h[child], child, path + [child])
                )


path = greedy(start, goal)

print("Path:", path)


# Draw graph
G = nx.Graph()

for node in graph:
    for child in graph[node]:
        G.add_edge(node, child)

pos = nx.spring_layout(G, seed=1)

# Node labels with heuristic
labels = {}

for node in graph:
    labels[node] = node + "\nh=" + str(h[node])

nx.draw(
    G,
    pos,
    with_labels=False,
    node_size=1500
)

nx.draw_networkx_labels(
    G,
    pos,
    labels=labels
)

plt.title("Greedy Best-First Search")
plt.show()