import numpy as np

f = open('input.txt', 'r')

counter = 0

def check_diffs(diffs):
    
    for num in diffs:
        if num > 3 or num <-3 or num == 0:
            return False

    if max(diffs) > 0 and min(diffs) < 0:
        return False
    
    return True

def calc_diffs(arr):

    diff_list = []
    for i, v in enumerate(arr):
        if i < len(arr) -1:
            diff_list.append(v-arr[i+1])

    return diff_list     


for x in f:
    
    arr = np.fromstring(x, sep=' ', dtype=int)
    
    if check_diffs(calc_diffs(arr)):
        counter += 1
        continue

    for i, r in enumerate(arr):
        if i < len(arr):
            n_array = np.delete(arr, i)
            diff_list = calc_diffs(n_array)
            if check_diffs(diff_list):
                counter += 1
                break

print(counter)