import itertools
def tsp(graph, start):
    n = len(graph)
    cities = list(range(n))
    permutations = itertools.permutations(cities)
    mincost = float('inf')
    minpath = None
    for path in permutations:
        path == (start,) + path
        cost = 0
        for i in range(n-1):
            cost += graph [path[i]] [path[i+1]]
        cost += graph [path[-1]][path[0]]
        if cost < mincost:
            mincost = cost
            minpath = path
    return mincost,minpath

graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

start_city = "A"
mincost,minpath = tsp(graph, start_city)

print("Minimum cost TSP: " , mincost)
print("Optimal pach: ", minpath)
