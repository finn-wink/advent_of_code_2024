import numpy as np
import heapq

def dijkstra(matrix, start, end):
    
    rows, cols = matrix.shape
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    distances = np.full((rows, cols), np.inf)
    distances[start] = 0

    # Priority queue for Dijkstra's algorithm (distance, (row, col))
    pq = [(0, start)]
    
    # To reconstruct the path
    parent = {start: None}

    while pq:
        current_distance, current_position = heapq.heappop(pq)
        row, col = current_position

        if current_position == end:
            break

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            new_position = (new_row, new_col)

            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row, new_col] == 0:
                
                # Implement check for the direction and add additional score if necessary
                new_distance = current_distance + 1

                if new_distance < distances[new_position]:
                    distances[new_position] = new_distance
                    heapq.heappush(pq, (new_distance, new_position))
                    parent[new_position] = current_position

    if distances[end] == np.inf:
        print("NO PATH")
        return None
    
    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()

    return path

def find_all_cheats(position, full_path, arr):
    
    rows, cols = arr.shape
    x, y = position

    cheat_positions = []

    for xx in range(-20, 21):
        for yy in range(-20, 21):
            if abs(xx) + abs(yy) <= 20:
                n_x, n_y = x + xx, y + yy
                if 0 <= n_x < rows and 0 <= n_y < cols and arr[(n_y, n_x)] != 1 and (n_y,n_x) not in FULL_PATH:
                    cheat_positions.append(n_x, n_y)

    return cheat_positions

f = open('input.txt', 'r')

arr_ls = []
dirs = []

for line in f:
    line_ls = []
    for char in line:
        if char == '#':
            line_ls.append(1)
        if char == '\n':
            continue
        if char == '.':
            line_ls.append(0)
        if char == 'S':
            line_ls.append(2)
        if char == 'E':
            line_ls.append(3)
    if line_ls != []:
        arr_ls.append(line_ls)

arr = np.array(arr_ls)

start_loc = np.where(arr == 2)
end_loc = np.where(arr == 3) 
start = (start_loc[0][0], start_loc[1][0])
end = ((end_loc[0][0], end_loc[1][0]))
arr[start] = 0
arr[end] = 0

solution = dijkstra(arr, start, end)
FULL_PATH_LENGTH = len(solution)
FULL_PATH = solution

len_finds = {}

test = find_all_cheats()

# For each position, find the positions that you can cheat to
# Check how fast each cheat is from that position
# Since there is only one path, ignore all the ones that are on the path

