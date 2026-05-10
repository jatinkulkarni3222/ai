class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            elif self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False


def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  # sort by weight

    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for u, v, w in edges:
        if ds.union(u, v):
            mst.append((u, v, w))
            total_weight += w

    return mst, total_weight


# ---- Taking Input ----
n, e = map(int, input("Enter number of vertices and edges: ").split())

edges = []
print("Enter edges (u v w):")
for _ in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# ---- Run Algorithm ----
mst, weight = kruskal(n, edges)

# ---- Output ----
print("\nMinimum Spanning Tree edges:")
for u, v, w in mst:
    print(f"{u} -- {v} == {w}")

print("Total weight of MST:", weight)

#Input:
# Enter number of vertices and edges: 4 5
# Enter edges (u v w):
# 0 1 10
# 0 2 6
# 0 3 5
# 1 3 15
# 2 3 4


#Output:
# Minimum Spanning Tree edges:
# 2 -- 3 == 4
# 0 -- 3 == 5
# 0 -- 1 == 10
# Total weight of MST: 19