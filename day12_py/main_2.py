import numpy as np

def search(pos, arr, visited, current):
    rows, cols = arr.shape
    stack = [pos]

    while stack:
        x, y = stack.pop()
        if (x, y) in visited:
            continue

        visited.add((x, y))
        current.append((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and arr[nx, ny] == arr[x, y] and (nx, ny) not in visited:
                stack.append((nx, ny))

    return current

with open('input.txt', 'r') as f:
    nums_dict = {}
    count = 0
    arr_arr = []

    for line in f:
        arr_line = []
        for c in line.strip():
            if c not in nums_dict:
                nums_dict[c] = count
                count += 1
            arr_line.append(nums_dict[c])
        arr_arr.append(arr_line)

arr = np.array(arr_arr)
# print(arr.shape[0])
# print(arr.shape[1])

visited = set()
unique = []

for r, row in enumerate(arr):
    for c, col in enumerate(row):
        if (r, c) not in visited:
            current = search((r, c), arr, visited, [])
            if current:
                unique.append(sorted(current))

pad_arr = np.pad(arr, pad_width=1, mode='constant', constant_values=100)

total_p = 0

for island in unique:
    sides = 0

    for y, x in island:
        py, px = y + 1, x + 1
        current_square = pad_arr[py, px] 

        up = False
        down = False
        right = False
        left = False

        if pad_arr[py + 1, px] == pad_arr[py, px]:
            down = True
        if pad_arr[py - 1, px] == pad_arr[py, px]:
            up = True
        if pad_arr[py, px + 1] == pad_arr[py, px]:
            right = True
        if pad_arr[py, px - 1] == pad_arr[py, px]:
            left = True

        dir_list = [up, down, left, right]
        print(dir_list)

        if not up and not down and not left and not right:
            sides += 4
        
        elif up and down and not left and not right or left and right and not up and not down:
            continue
        
        elif dir_list.count(True) == 2:
            sides += 1
        
        elif dir_list.count(True) == 1:
            sides += 2

    print(island)
    print(sides)


# print("Result 2" + str(sides))

# print(unique)

####

# Corners:
#   #
   #A# - 2

    #
# 1 A 1 - 0
# 1 A 1 

# If there are 2 sides, that are next to each other, it's 1
# If it's an end-piece there is 2
# If there is a piece on either side, it's 0
# If it's everywhere, it's 4