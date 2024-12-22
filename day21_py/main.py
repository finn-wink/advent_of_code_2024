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

    if len(path) == 1:
        moves.append(5)
        return moves

    for i, m in enumerate(path):
        if i == path_length - 1:
            moves.append(5) # ENTER -> A
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

def moves_to_dir(moves):

    dir_positions = []

    for m in moves:
        if m == 1:
            dir_positions.append((0,1))
        if m == 2:
            dir_positions.append((1,0))
        if m == 3:
            dir_positions.append((1,1))
        if m == 4:
            dir_positions.append((1,2))
        if m == 5:
            dir_positions.append((0,2))

    return dir_positions

def get_shortest_paths(paths):

    shortest_len = min(len(path) for path in paths) # Find the shortest length
    shortest_paths = [p for p in paths if len(p) == shortest_len] # Get all paths with shortest length 

    return shortest_paths

def find_num_paths(numpad, current, to_find, forbidden):

    new_y, new_x = np.where(numpad == to_find)

    all_paths = find_all_paths(numpad, current, (new_y[0], new_x[0]), forbidden)
    shortest_paths = get_shortest_paths(all_paths)
    
    shortest_moves = []
    for s in shortest_paths:
        shortest_moves.append(path_to_moves(s))

    return shortest_moves


def find_dir_paths(dirpad, curr_pos, moves, forbid_dir):
    
    dir_pos = moves_to_dir(moves)
    # print(dir_pos)
    possible_paths = []

    for i, dp in enumerate(dir_pos):
        if i < len(dir_pos) - 1 and dp == dir_pos[i-1]:
            possible_paths.append([[dp]])
            continue
        elif i == 0:
            all_paths = find_all_paths(dirpad, curr_pos, dp, forbid_dir)
        else:
            all_paths = find_all_paths(dirpad, dir_pos[i-1], dp, forbid_dir)
        # print(dir_pos[i-1])
        # print(dp)
        pp = get_shortest_paths(all_paths)
        possible_paths.append(pp)

        possible_directions = []

        for pp in possible_paths:
            dir_group = []
            for dd in pp:
                dir_group.append(path_to_moves(dd))
            possible_directions.append(dir_group)

    return possible_directions

# code_to_check = [0, 2, 9, 10] # Translate codes into numbers
code_to_check = [0, 2, 9, 10]

num_pad = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3], [100, 0, 10]])
dir_pad = np.array([[100, 1, 10], [2, 3, 4]])

# press_number = (0,2)

dir_pad_me = (0,2)
dir_pad_robot1 = (0,2)
dir_pad_robot2 = (0,2)
num_pad_pos = (3,2)

forbid_num = (3,0)
forbid_dir = (0,0)

full1 = []

for num in code_to_check:
    directions = find_num_paths(num_pad, num_pad_pos, num, forbid_num)
    directions1 = find_dir_paths(dir_pad, dir_pad_robot1, directions[0], forbid_dir)
    for d1 in directions1:
        directions2 = find_dir_paths(dir_pad, dir_pad_robot2, d1[0], forbid_dir)
        for d2 in directions2:
            directions3 = find_dir_paths(dir_pad, dir_pad_me, d2[0], forbid_dir)
            for d3 in directions3:
                full1.append(d3[0])

count = 0
for tt in full1:
    for zz in tt:
        count+=1

print(count)
# print(count)
# print(full_moves)

# print(directions)
# print(directions1)
# print(directions2)
# print(directions_me)
