import numpy as np


def search(pos, arr, visited, current):

    up = (pos[0]-1, pos[1])
    down = (pos[0]+1, pos[1])
    right = (pos[0], pos[1]+1)
    left = (pos[0], pos[1]-1)

    if pos not in visited:
        current.append(pos)
        visited.append(pos)

        if up[0] != -1:
            if arr[up[0], up[1]] == arr[pos[0], pos[1]]:
                current = search(up, arr, visited, current)
        if down[0] != arr.shape[0]:
            if arr[down[0], down[1]] == arr[pos[0], pos[1]]:
                current = search(down, arr, visited, current)
        if right[1] != arr.shape[1]:
            if arr[right[0], right[1]] == arr[pos[0], pos[1]]:
                current = search(right, arr, visited, current)
        if left[1] != 0:
            if arr[left[0], left[1]] == arr[pos[0], pos[1]]:
                current = search(left, arr, visited, current)

    return current

f = open('input.txt', 'r')

nums_dict = {}
count = 0

arr_arr = []

for line in f:
    arr_line = []
    for c in line:
        if c == '\n':
            continue
        if c not in nums_dict.keys():
            nums_dict[c] = count
            count += 1
        arr_line.append(nums_dict[c])
    arr_arr.append(arr_line)

arr = np.array(arr_arr)
print(arr.shape[0])
print(arr.shape[1])

visited = []
unique = []

for r, row in enumerate(arr):
    for c, col in enumerate(row):
        current = []
        current = search((r, c), arr, visited, current)
        if current != [] and current not in unique:
            unique.append(current)

pad_arr = np.pad(arr, pad_width=1, mode='constant', constant_values=100)

total_island = 0

for islands in unique:
    print(len(islands))
    
    total_island += len(islands)

print(total_island)

total_p = 0

# Found unique islands
for island in unique:
    perimeter = 0
    area = 0
    for p in island:
        area += 1
        new = (p[0]+1, p[1]+1)
        p = 4
        if pad_arr[new[0]+1][new[1]] == pad_arr[new[0]][new[1]]:
            p -= 1
        if pad_arr[new[0]-1][new[1]] == pad_arr[new[0]][new[1]]:
            p -= 1
        if pad_arr[new[0]][new[1]+1] == pad_arr[new[0]][new[1]]:
            p -= 1
        if pad_arr[new[0]][new[1]-1] == pad_arr[new[0]][new[1]]:
            p -= 1   
        perimeter += p
    total_p += area * perimeter

print(total_p)