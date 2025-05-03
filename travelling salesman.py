import itertools

dist = {
    ('A','B'):10, ('A','C'):15, ('A','D'):20,
    ('B','C'):35, ('B','D'):25,
    ('C','D'):30
}
dist.update({(b,a):d for (a,b),d in dist.items()})  # Symmetric

cities = ['A','B','C','D']
min_cost = float('inf')

for p in itertools.permutations(cities[1:]):
    path = ['A'] + list(p) + ['A']
    cost = sum(dist[(path[i], path[i+1])] for i in range(4))
    if cost < min_cost:
        min_cost = cost
        best = path

print("Path:", " -> ".join(best))
print("Cost:", min_cost)
