import random

def random_search(graph, start_node, goal_node):
    visited = set()
    stack = [start_node]

    while stack:
        current_node = stack.pop()
        if current_node == goal_node:
            print("Goal node reached!")
            return True  # Goal reached

        if current_node not in visited:
            visited.add(current_node)
            print("Visiting node:", current_node)

            unvisited_neighbors = [neighbor for neighbor in graph[current_node] if neighbor not in visited]
            stack.extend(unvisited_neighbors)

    print("Goal node not reached.")
    return False  

# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# # Choose a random starting node and goal node
# start_node = random.choice(list(graph.keys()))
# goal_node = random.choice(list(graph.keys()))

# # Perform a random search between the start and goal nodes
# random_search(graph, start_node, goal_node)
