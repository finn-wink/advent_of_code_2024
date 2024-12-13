import numpy as np

f = open('input.txt', 'r')

nums_dict = {}
count = 0

arr_arr = []

for line in f:
    arr_line = []
    for c in line:
        if c not in nums_dict.keys():
            nums_dict[c] = count
            count += 1
        arr_line.append(nums_dict[c])
    arr_arr.append(arr_line)

arr = np.array(arr_arr)

pos_list = [] # Position of the same letters

for k in nums_dict.values():
    _temp = []
    for i, row in enumerate(arr):
        for j, col in enumerate(row):
            if col == k:
                _temp.append((i,j))
    pos_list.append(_temp)

groups = []

# If diff bigger, then append list, else append value


