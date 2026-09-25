import heapq
import networkx as nx
import matplotlib.pyplot as plt

graph = {}

e = int(input("Number of edges: "))

for i in range(e):
    u, v, cost = input("Edge: ").split()
    cost = int(cost)

    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append((v, cost))
    graph[v].append((u, cost))


h = {}

for node in graph:
    h[node] = int(input("h(" + node + "): "))


start = input("Start: ")
goal = input("Goal: ")


def a_star(start, goal):

    pq = [(h[start], 0, start, [start])]
    visited = set()

    while pq:

        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        print("Expand:", node, "g =", g,
              "h =", h[node], "f =", f)

        if node == goal:
            return path, g

        for child, cost in graph[node]:

            if child not in visited:
                new_g = g + cost
                new_f = new_g + h[child]

                heapq.heappush(
                    pq,
                    (new_f, new_g, child, path + [child])
                )


print("A* Result:", a_star(start, goal))


# Graph
G = nx.Graph()

for node in graph:
    for child, cost in graph[node]:
        G.add_edge(node, child, weight=cost)

pos = nx.spring_layout(G, seed=1)

# Node + heuristic
labels = {}

for node in graph:
    labels[node] = node + "\nh=" + str(h[node])

nx.draw(G, pos, with_labels=False, node_size=1500)

nx.draw_networkx_labels(G, pos, labels)

# Edge cost
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

plt.show()