''' 
- M represents the number of missionaries on the starting side of the river.
- C represents the number of cannibals on the starting side of the river.
- B represents the position of the boat: B = 1 if the boat is on the starting side, and B = 0 
if the boat is on the destination side.

- Initial State: (3, 3, 1)
- Goal State: (0, 0, 0)

The possible combination of actions are:

(1, 0, 1) - Send one missionary across.
(2, 0, 1) - Send two missionaries across.
(0, 1, 1) - Send one cannibal across.
(0, 2, 1) - Send two cannibals across.
(1, 1, 1) - Send one missionary and one cannibal across.

- Constraints:
At any point, the number of missionaries and cannibals on either side of the river cannot be 
outnumbered by the cannibals. Otherwise, the missionaries will be eaten.
'''


from collections import deque
# Function to check validity of the state. 
def is_valid_state(state):
    m, c, b = state
    if m < 0 or m > 3 or c < 0 or c > 3: 
        return False
    if m > 0 and m < c: # More cannibals than missionaries on starting side
        return False
    if m < 3 and m < c: # More cannibals than missionaries on ending side
        return False
    return True

# Function that generate valid states
def successors(state):
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)] # no. of M and C moved in that action
    m, c, b = state
    for move in moves:
        if b == 1: # if boat is on the starting side
            new_state = (m - move[0], c - move[1], 0) # calculates new state after applying the move
        else:
            new_state = (m + move[0], c + move[1], 1) # calculates new state after applying the move
        # checks if the new state is valid state or not
        if is_valid_state(new_state):
            yield new_state # yeild = returns list of values

def bfs():
    start_state = (3, 3, 1)
    goal_state = (0, 0, 0)
    queue = deque([(start_state, [])]) # initializes a queue with the start state and an empty path
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        visited.add(state)
        for successor_state in successors(state):
            if successor_state not in visited:
                queue.append((successor_state, path + [successor_state]))

solution = bfs()
for i, state in enumerate(solution):
    print(f"Step {i+1}: {state}")
