# Small Map Coloring CSP with 3 regions

# Define neighbors
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

# Define colors
colors = ['Red', 'Green']

# Check constraints
def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking CSP solver
def backtrack(assignment):
    if len(assignment) == len(neighbors):
        return assignment

    region = [r for r in neighbors if r not in assignment][0]
    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]  # backtrack
    return None

# Run the solver
solution = backtrack({})
print("Solution:", solution if solution else "No solution found")
