import numpy as np
import copy

# Go until there is nothing and note down intersections
# If it doesn't work, go back to intersection and try again
    # Mark all the possible turn offs?

def find_direction(current, new):

    direction_diff = tuple(np.subtract(current, new)) 
    # print(direction_diff)
    # Determine direction
    if direction_diff[0] == 0:
        if direction_diff[1] == 1:
            return 3
        if direction_diff[1] == -1:
            return 2
    if direction_diff[1] == 0:
        if direction_diff[0] == 1:
            return 0
        if direction_diff[0] == -1:
            return 1    

def find_shortest_path(paths):

    if len(paths) == 1: # if only one path
        return 0, paths[0]

    else:
        lowest_value = 0
        for i, p in enumerate(paths):
            if lowest_value == 0 or p[2] < lowest_value:
                lowest_value = p[2]
                lowest_path = p
                path_index = i
        
        return path_index, lowest_path


def dijkstra(maze, current, end):

    solved = False
    direction = 2 # Up = 0, Down = 1, Right = 2, Left = 3 
    cur_new_path = 0
    
    paths = []

    path1 = []
    path1.append((current[0][0], current[1][0])) # Current position [0]
    path1.append(2) # Direction [1]
    path1.append(0) # Score [2]
    path1.append([]) # Visited [3]
    
    paths.append(path1)
    
    # global_visited = set()

    count = 0
    
    while not solved:
        
        # Take the shortest path
        path_index, shortest = find_shortest_path(paths)
     
        up = (shortest[0][0]-1, shortest[0][1])
        down = (shortest[0][0]+1, shortest[0][1])
        right = (shortest[0][0], shortest[0][1]+1)
        left = (shortest[0][0], shortest[0][1]-1)

        check_list = [up, down, right, left]

        found = []

        # for check in check_list:
        #     if maze[check] == 0 and check not in global_visited:
        #         found.append(check)
        #         global_visited.add(check)
        #     if maze[check] == 1:
        #         return shortest

        for check in check_list:
            if maze[check] == 0:
                found.append(check)
            if maze[check] == 1:
                return shortest

        keep_position = shortest[0]
        keep_direction = shortest[1]
        keep_score = shortest[2]
        print(keep_position)
        print(len(paths))

        # found_f = [item for item in found if item not in shortest[3]]
        found_f = found

        if len(found_f) == 0:
            del paths[path_index]
            continue
        
        # print(found_f)
        for i, ff in enumerate(found_f):
            if i == 0:
                direc = find_direction(shortest[0], ff)

                if direc != shortest[2]:
                    paths[path_index][2] += 1001
                    paths[path_index][1] = direc
                else:
                    paths[path_index][2] += 1
                
                paths[path_index][0] = ff
                paths[path_index][3].append(ff)
                
            else:
                new_path = []
                new_path.append(ff)

                direc = find_direction(keep_position, ff)
                new_path.append(direc)
                new_path.append(keep_score)

                if direc != keep_direction:
                    new_path[2] += 1001
                else:
                    new_path[2] += 1
                
                new_path.append(paths[path_index][3][1:])
                new_path[3].append(ff)

                paths.append(new_path)
                # print(paths)
      
        # print(paths)
            # print(paths)

f = open('input.txt', 'r')

arr_ls = []
dirs = []

for line in f:
    line_ls = []
    for char in line:
        if char == '#':
            line_ls.append(5)
        if char == '.':
            line_ls.append(0)
        if char == 'E':
            line_ls.append(1)
        if char == 'S':
            line_ls.append(2)
    if line_ls != []:
        arr_ls.append(line_ls)

arr = np.array(arr_ls)
start = np.where(arr == 2)
end = np.where(arr== 1)

shortest_path = dijkstra(arr, start, end)

print(shortest_path)
# print(shortest_path)
# # Check the next positions
# # If it is 0, add to current path, add 1 to the path
# # Dictionary -> Score, current position
# # Add new record to dictionary, or update dictionary