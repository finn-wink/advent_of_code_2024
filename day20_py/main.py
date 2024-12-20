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
    
    print(current_distance)

    path = []
    step = end
    while step is not None:
        path.append(step)
        step = parent[step]
    path.reverse()

    return path

f = open('input.txt', 'r')

arr_ls = []
dirs = []

for line in f:
    line_ls = []
    for char in line:
        if char == '#':
            line_ls.append(1)
        else:
            line_ls.append(0)
    if line_ls != []:
        arr_ls.append(line_ls)

start = (7,5)
end = (3,1)
arr = np.array(arr_ls)

solution = dijkstra(arr, start, end)

