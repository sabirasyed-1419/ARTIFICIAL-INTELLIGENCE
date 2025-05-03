import heapq

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g = g[current] + 1
                if tentative_g < g.get(neighbor, float('inf')):
                    g[neighbor] = tentative_g
                    heapq.heappush(open_set, (tentative_g + heuristic(neighbor, goal), neighbor))
                    came_from[neighbor] = current
    return []

# 0 = free, 1 = wall
grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0]]
start, goal = (0, 0), (2, 2)

path = astar(grid, start, goal)
print("Path:", path)
