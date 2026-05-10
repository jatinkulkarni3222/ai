import heapq

def dijkstra(n, adj, source):
    dist = [float('inf')] * n
    dist[source] = 0

    min_heap = [(0, source)]  # (distance, node)

    while min_heap:
        d, node = heapq.heappop(min_heap)

        if d > dist[node]:
            continue

        for neighbor, weight in adj[node]:
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(min_heap, (dist[neighbor], neighbor))

    return dist


# ---- Input ----
n, e = map(int, input("Enter number of vertices and edges: ").split())

adj = [[] for _ in range(n)]

print("Enter edges (u v w):")
for _ in range(e):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))  # remove this line if graph is directed

source = int(input("Enter source node: "))

# ---- Run ----
distances = dijkstra(n, adj, source)

# ---- Output ----
print("\nShortest distances from source:")
for i in range(n):
    print(f"{source} → {i} = {distances[i]}")

# Enter number of vertices and edges: 5 6
# Enter edges (u v w):
# 0 1 4
# 0 2 1
# 2 1 2
# 1 3 1
# 2 3 5
# 3 4 3
# Enter source node: 0

#O/P:

# Shortest distances from source:
# 0 → 0 = 0
# 0 → 1 = 3
# 0 → 2 = 1
# 0 → 3 = 4
# 0 → 4 = 7