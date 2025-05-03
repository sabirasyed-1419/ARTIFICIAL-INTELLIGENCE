from collections import deque
def bfs(start, goal):
    queue = deque([(start, [])])
    visited = set([start])
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path + [state]
        z = state.index(0)
        x, y = divmod(z, 3)
        for dx, dy in moves:
            nx, ny = x+dx, y+dy
            if 0<=nx<3 and 0<=ny<3:
                nz = nx*3 + ny
                new = list(state)
                new[z], new[nz] = new[nz], new[z]
                new_t = tuple(new)
                if new_t not in visited:
                    visited.add(new_t)
                    queue.append((new_t, path + [state]))
    return None

start = (1,2,3,4,0,5,6,7,8)
goal = (1,2,3,4,5,0,6,7,8)
res = bfs(start, goal)

if res:
    for s in res:
        print(s[0:3], s[3:6], s[6:9], sep="\n")
        print()
else:
    print("No solution.")
