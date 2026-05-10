import heapq

# Goal State
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Directions (Up, Down, Left, Right)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


class Node:
    def __init__(self, state, g, h, x, y, parent):
        self.state = state
        self.g = g  # cost so far
        self.h = h  # heuristic
        self.x = x  # blank tile position
        self.y = y
        self.parent = parent

    def f(self):
        return self.g + self.h

    # For priority queue (min-heap)
    def __lt__(self, other):
        return self.f() < other.f()


# Manhattan Distance Heuristic
def calculate_heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                val = state[i][j]
                target_x = (val - 1) // 3
                target_y = (val - 1) % 3
                h += abs(i - target_x) + abs(j - target_y)
    return h


# Convert state to string for hashing
def state_to_string(state):
    return ''.join(str(num) for row in state for num in row)


# Print solution path
def print_path(node):
    path = []

    while node:
        path.append(node.state)
        node = node.parent

    path.reverse()

    for state in path:
        for row in state:
            print(*row)
        print("------")


# A* Algorithm
def astar(start):
    visited = set()
    pq = []

    # Find blank (0) position
    for i in range(3):
        for j in range(3):
            if start[i][j] == 0:
                x, y = i, j

    root = Node(start, 0, calculate_heuristic(start), x, y, None)
    heapq.heappush(pq, root)

    while pq:
        curr = heapq.heappop(pq)
        key = state_to_string(curr.state)

        if key in visited:
            continue
        visited.add(key)

        if curr.state == goal:
            print("Solution found!\n")
            print_path(curr)
            return

        # Explore neighbors
        for i in range(4):
            nx = curr.x + dx[i]
            ny = curr.y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in curr.state]
                # Swap blank
                new_state[curr.x][curr.y], new_state[nx][ny] = \
                    new_state[nx][ny], new_state[curr.x][curr.y]

                new_key = state_to_string(new_state)

                if new_key not in visited:
                    child = Node(
                        new_state,
                        curr.g + 1,
                        calculate_heuristic(new_state),
                        nx,
                        ny,
                        curr
                    )
                    heapq.heappush(pq, child)

    print("No solution exists!")


# Main function
def main():
    start = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 5, 8]
    ]

    astar(start)


if __name__ == "__main__":
    main()


# python3 Assignment2.py
# Solution found!

# 1 2 3
# 4 0 6
# 7 5 8
# ------
# 1 2 3
# 4 5 6
# 7 0 8
# ------
# 1 2 3
# 4 5 6
# 7 8 0
# ------
