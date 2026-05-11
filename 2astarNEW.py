import heapq

GOAL_STATE = [[1,2,3],[4,5,6],[7,8,0]]
MOVES = [(-1,0),(1,0),(0,-1),(0,1)]

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                value = state[i][j]
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

def to_tuple(state):
    return tuple(tuple(row) for row in state)

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def a_star(start):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start), 0, start))
    visited = set()
    parent = {}

    while open_list:
        f, g, current = heapq.heappop(open_list)

        if current == GOAL_STATE:
            return reconstruct_path(parent, current)

        visited.add(to_tuple(current))

        for neighbor in get_neighbors(current):
            if to_tuple(neighbor) not in visited:
                parent[to_tuple(neighbor)] = current
                heapq.heappush(open_list,
                    (g+1 + manhattan_distance(neighbor), g+1, neighbor))
    return None

def reconstruct_path(parent, current):
    path = [current]
    while to_tuple(current) in parent:
        current = parent[to_tuple(current)]
        path.append(current)
    return path[::-1]

start = [[1,2,3],[4,0,6],[7,5,8]]
solution = a_star(start)

for step in solution:
    for row in step:
        print(row)
    print("-----")