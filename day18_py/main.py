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

f = open('input.txt', 'r')

matrix = np.zeros((71,71))

num_list = []

for i, line in enumerate(f):
    
    nums = line.strip().split(',')
    num_list.append((nums[0], nums[1]))

solved = False
search_start = 1024

# Initialize matrix
for x in num_list[:2940]:
    matrix[(int(x[1]), int(x[0]))] = 1

# while not solved:

#     for y in range(1025, len(num_list), 10):
#         for x in num_list[search_start:y]:
#             matrix[(int(x[1]), int(x[0]))] = 1

#     start = (0,0)
#     end = (70,70)

#     result = dijkstra(matrix, start, end)

#     if result == None:
#         print(y)

start = (0,0)
end = (70,70)

result = dijkstra(matrix, start, end)

print(result)
print(num_list[:2941])