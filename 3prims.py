import heapq

def prims_adj_list(n, adj):
    visited = [False] * n
    min_heap = [(0, 0, -1)]  # (weight, node, parent)

    mst = []
    total_weight = 0

    while min_heap and len(mst) < n:
        weight, node, parent = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True
        total_weight += weight

        if parent != -1:
            mst.append((parent, node, weight))

        for neighbor, wt in adj[node]:
            if not visited[neighbor]:
                heapq.heappush(min_heap, (wt, neighbor, node))

    return mst, total_weight


# ---- Input ----
n, e = map(int, input("Enter number of vertices and edges: ").split())

adj = [[] for _ in range(n)]

print("Enter edges (u v w):")
for _ in range(e):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))  # undirected graph

# ---- Run ----
mst, weight = prims_adj_list(n, adj)

# ---- Output ----
print("\nMST edges:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")

print("Total weight:", weight)


#I/P

# Enter number of vertices and edges: 5 7
# Enter edges (u v w):
# 0 1 2
# 0 3 6
# 1 2 3
# 1 3 8
# 1 4 5
# 2 4 7
# 3 4 9

# After input, the graph internally looks like:
# 0 → (1,2), (3,6)
# 1 → (0,2), (2,3), (3,8), (4,5)
# 2 → (1,3), (4,7)
# 3 → (0,6), (1,8), (4,9)
# 4 → (1,5), (2,7), (3,9)


#O/P:

# MST edges:
# 0 -- 1 == 2
# 1 -- 2 == 3
# 1 -- 4 == 5
# 0 -- 3 == 6

# Total weight: 16