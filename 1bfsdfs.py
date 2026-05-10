from collections import deque

def dfs(node, adj, visited):
    visited[node] = True
    print(node, end=" ")

    for nbr in adj[node]:
        if not visited[nbr]:
            dfs(nbr, adj, visited)


def bfs(start, adj, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()
        print(node, end=" ")

        for nbr in adj[node]:
            if not visited[nbr]:
                visited[nbr] = True
                q.append(nbr)


def main():

    V = int(input("Enter number of vertices: "))

    adj = [[] for _ in range(V)]

    E = int(input("Enter number of edges: "))

    print("Enter edges:")

    # Input edges
    for _ in range(E):
        u, v = map(int, input().split())

        # Undirected graph
        adj[u].append(v)
        adj[v].append(u)

    # Starting node
    start = int(input("Enter starting node: "))

    # DFS
    visited = [False] * V
    print("DFS :", end=" ")
    dfs(start, adj, visited)

    # BFS
    visited = [False] * V
    print("\nBFS :", end=" ")
    bfs(start, adj, visited)

    print()


if __name__ == "__main__":
    main()

# python3 Assignment1.py 
# DFS : 0 1 3 2 4 
# BFS : 0 1 2 3 4 