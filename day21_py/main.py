import numpy as np
import heapq

CODES = ['029A', '980A', '179A', '456A', '379A']

def find_all_paths(grid, start, end, forbidden):
    
    def is_valid_move(pos, visited):
        row, col = pos
        if row < 0 or row >= grid.shape[0] or col < 0 or col >= grid.shape[1]:
            return False
        if pos in visited:
            return False
        if (row, col) in forbidden:
            return False
        return True
    
    def dfs(current, visited, path):
        if current == end:
            return [path[:]]
        
        paths = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for dx, dy in directions:
            next_pos = (current[0] + dx, current[1] + dy)
            if is_valid_move(next_pos, visited):
                visited.add(next_pos)
                path.append(next_pos)
                paths.extend(dfs(next_pos, visited, path))
                path.pop()
                visited.remove(next_pos)
                
        return paths
    
    visited = {start}
    initial_path = [start]
    
    return dfs(start, visited, initial_path)


def path_to_moves(path):
    
    path_length = len(path)
    moves = []

    for i, m in enumerate(path):
        if i == path_length - 1:
            break
    
        direction_diff = tuple(np.subtract(path[i+1], m)) 
        if direction_diff == (0,1):
            moves.append(4) # Right
        if direction_diff == (0,-1):
            moves.append(2) # Left
        if direction_diff == (1,0):
            moves.append(3)# Down
        if direction_diff == (-1,0):
            moves.append(1) # Up

    return moves

def find_shortest_paths(numpad, current, to_find, forbidden):

    new_y, new_x = np.where(numpad == to_find)

    all_paths = find_all_paths(numpad, current, (new_y[0], new_x[0]), forbidden)
    shortest_len = min(len(path) for path in all_paths) # Find the shortest length
    shortest_paths = [p for p in all_paths if len(p) == shortest_len] # Get all paths with shortest length

    moves = shor

    return shortest_paths


# Figure out all the possible moves to get from one to the other
# Take only the shortest
# Keep only the shortest ones
# Use those to find all possible moves in the next one
# Keep only the shortest ones


# code_to_check = [0, 2, 9, 10] # Translate codes into numbers
code_to_check = [9]

num_pad = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3], [100, 0, 10]])
dir_pad = np.array([[100, 1, 10], [2, 3, 4]])

press_number = (0,2)

dir_pad_me = (0,2)
dir_pad_robot1 = (0,2)
dir_pad_robot2 = (0,2)
num_pad_pos = (3,1)

do_not_go = (3,0)

for num in code_to_check:
    directions = find_shortest_paths(num_pad, num_pad_pos, num, do_not_go)
    # for d in directions:
    #     directions1 = find_path(dir_pad, dir_pad_robot2, d)

        # for d1 in directions1:
        #     directions2 = find_path(dir_pad, dir_pad_robot1, d1)
        #     for d2 in directions2:
        #         directions_me = find_path(dir_pad, dir_pad_me, d2)
    break

print(directions)
# print(directions1)
# print(directions2)
# print(directions_me)
