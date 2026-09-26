import networkx as nx
import matplotlib.pyplot as plt

graph = {}

# Edge input
e = int(input("Number of edges: "))

for i in range(e):
    u, v = input("Edge (u,v): ").split()

    if u not in graph:
        graph[u] = []

    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u) 


def dfs(start, goal):
	stack = [(start, [start])]
	visited = set()
	while stack:
		node, path = stack.pop()
		print("Expand:", node, "\nStack:", list(stack))
		if node == goal:
			return path
		if node not in visited:
			visited.add(node)
			# Reverse so leftmost child is processed first
			for child in reversed(graph[node]):
				if child not in visited:
					stack.append((child, path + [child]))
start = input("Start: ")
goal = input("Goal: ")
print("DFS Path:", dfs(start, goal))

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

plt.title("DFS Graph")
plt.show()