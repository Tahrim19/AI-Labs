import msvcrt
import os
from collections import deque #  double-ended queue used as a stack for DFS exploration.

def DFS(maze, start=(0, 0), goal=(7, 11)):
  stack = deque([start])
  visited = set()  

  while stack:
    row, col = stack.pop()

    # Check for base cases
    if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]) or maze[row][col] == 0:
      continue
    if (row, col) == goal:
      path = []
      while stack:
        path.append(stack.pop())
      path.append((row, col))  # Add goal to path
      path.reverse()  # Reverse path for correct order
      return path
    if (row, col) in visited:
      continue

    visited.add((row, col))

    # Explore valid neighbors using a stack
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Up, right, down, left
    for dr, dc in directions:
      next_row, next_col = row + dr, col + dc
      stack.append((next_row, next_col))

  return None  # No path found
 

''' 
. : Represents valid path
# : Represents invalid path

'''

maze = [
    ['.', '#', '.', '#', '#', '.', '#', '.', '#', '.', '.', '#'],
    ['.', '#', '.', '#', '.', '.', '#', '#', '.', '.', '.', '#'],
    ['.', '#', '#', '.', '#', '#', '.', '#', '#', '#', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '#', '.', '.', '.', '#'],
    ['.', '.', '.', '.', '#', '.', '.', '.', '#', '#', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '#', '.', '.', '.', '#', '.'],
    ['#', '#', '#', '.', '.', '.', '#', '#', '#', '.', '.', '.'],
    ['.', '.', '#', '#', '.', '.', '.', '.', '#', '.', '#', 'E']
]

path = DFS(maze)

if path:
  print("Path found")
else:
  print("No path found")



# # function for printing the amze
# def printMaze():
#   for row in maze:
#       print(' '.join(map(str, row)))
  
def printMaze():
  os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
  for i in range(len(maze)):  # Use maze length for rows
    for j in range(len(maze[0])):  # Use first row length for columns
      if (i, j) == user_pos:
        print('R', end=' ')  # Print user's position
      else:
        print(maze[i][j], end=' ')
    print()




user_pos = (0, 0)

# checking if move is valid:
def is_valid_move(position, row, col):
  x, y = position
  return 0 <= x < row and 0 <= y < col and maze[x][y] != '#'


# movement through the maze:
def move(direction):
    global user_pos
    x, y = user_pos
    if direction == b'w':    # up
        new_pos = (x-1, y)
    elif direction == b's':  # down
        new_pos = (x+1, y)
    elif direction == b'a':  # left
        new_pos = (x, y-1)   
    elif direction == b'd':  # right
        new_pos = (x, y+1)   
    else:
        return
    
    if is_valid_move(new_pos, len(maze), len(maze[0])):
      user_pos = new_pos
      printMaze()


# play game:
def play():
        printMaze()
        while True:
            direction = msvcrt.getch()
            if direction == b'q':  # Quit if 'q' is pressed
              print("Game Quit.")
              break          
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal
            move(direction)
            printMaze()
            if maze[user_pos[0]][user_pos[1]] == 'E':
              print("Exit reached!")
              break
            


play()