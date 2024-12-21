iimport numpy as np

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
print(arr.shape[0])
print(arr.shape[1])

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
    perimeter = 0
    area = len(island)

    for x, y in island:
        px, py = x + 1, y + 1
        p = 4

        if pad_arr[px + 1, py] != pad_arr[px, py]:
            
        if pad_arr[px - 1, py] == pad_arr[px, py]:
            p -= 1
        if pad_arr[px, py + 1] == pad_arr[px, py]:
            p -= 1
        if pad_arr[px, py - 1] == pad_arr[px, py]:
            p -= 1

        perimeter += p

print("Result 1" + str(total_p))

print(unique)

####