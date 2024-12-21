import numpy as np

def find_gap(array, file):

    for i, p in enumerate(array):
        if i == file[1]['start']:
            return array

        if p != -1:
            space_count = 0

        if p == -1:
            space_count += 1
            if space_count == file[1]['length']:
                array[array == file[0]] = -1
                array[i-file[1]['length']+1:i+1] = file[0]
                return array

    return array

f = open('input.txt', 'r')

all_symbols = {}
symbol_int = 0

pattern = []
nums = []
full = []

for line in f:
    for i, c in enumerate(line):
        if i % 2 == 0:
            nums.extend([i/2]*int(c))
            pattern.extend([0]*int(c)) # 0 is file
            

        if i % 2 != 0:
            pattern.extend([-1]*int(c)) # 1 is space

new_arr = []

files = {}

n_index = 0
for index, p in enumerate(pattern):
    if p == 0:
        new_arr.append(nums[n_index])
        if nums[n_index] not in files:
            files[nums[n_index]] = {}
            files[nums[n_index]]['start'] = index
            files[nums[n_index]]['length'] = 1
        else:
            files[nums[n_index]]['length'] += 1
        n_index += 1
    if p == -1:
        new_arr.append(p)

r_files = dict(reversed(files.items()))

np_arr = np.array(new_arr)
r_np_arr = np_arr[::-1].copy()

for ff in r_files.items():
    np_arr = find_gap(np_arr, ff)

np_arr[np_arr == -1] = 0

total = 0
for ind, num in enumerate(np_arr):
    total += ind * num

print(np_arr)
print(total)