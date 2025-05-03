def water_jug(x, y, target):
    visited = set()
    stack = [(0, 0)]
    while stack:
        a, b = stack.pop()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        if a == target or b == target:
            print("Solution:", (a, b))
            return
        stack.extend([
            (x, b), (a, y), (0, b), (a, 0),
            (min(a + b, x), b - (min(a + b, x) - a)) if b else (a, b),
            (a - (min(a + b, y) - b), min(a + b, y)) if a else (a, b)
        ])
    print("No solution.")

water_jug(4, 3, 2)
