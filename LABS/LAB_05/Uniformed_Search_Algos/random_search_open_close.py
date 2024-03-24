import random

def random_search(graph, start, goal):
    open_list = [start]
    closed_list = []
    goal_path = []

    # until open_list is not empty
    while open_list:
        print("Open List:", open_list)
        print("Closed List:", closed_list)
        
        current_node = random.choice(open_list)
        open_list.remove(current_node)

        if current_node == goal:
            goal_path.append(current_node)
            print("Goal Path:", goal_path)
            return "Goal found"

        closed_list.append(current_node)
        goal_path.append(current_node)

        # Explore the neighbors of the chosen node
        neighbors = graph[current_node]
        for i in neighbors:
            # If a neighbor is not already visited, add it to the open list
            if i not in closed_list and i not in open_list:
                open_list.append(i)

    return "Goal not found"

# Graph:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Define the start node and the goal node
start_node = 'A'
goal_node = 'F'

result = random_search(graph, start_node, goal_node)

print(result)
