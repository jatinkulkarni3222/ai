def is_safe(node, graph, color, c, V):

    for k in range(V):

        if graph[node][k] == 1 and color[k] == c:
            return False

    return True



def graph_coloring(graph, m, color, node, V):

    if node == V:
        return True

    # Try all colors
    for c in range(1, m + 1):

        if is_safe(node, graph, color, c, V):

            color[node] = c

            # Recursive call
            if graph_coloring(graph, m, color, node + 1, V):
                return True

            # Backtrack
            color[node] = 0

    return False


# Main Function
def main():

    # Number of vertices
    V = int(input("Enter number of vertices: "))

    # Number of colors
    m = int(input("Enter number of colors: "))

    # Adjacency matrix
    graph = []

    print("Enter adjacency matrix:")

    for i in range(V):
        row = list(map(int, input().split()))
        graph.append(row)

    color = [0] * V

    # Start coloring
    if graph_coloring(graph, m, color, 0, V):

        print("\nSolution Exists!")

        for i in range(V):
            print(f"Vertex {i} ---> Color {color[i]}")

    else:
        print("No Solution Exists")


if __name__ == "__main__":
    main()