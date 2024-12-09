import numpy as np

f = open('input.txt', 'r')

all_symbols = {}
symbol_int = 0

pattern = []
nums = []

for line in f:
    for i, c in enumerate(line):
        if i % 2 == 0:
            nums.extend([i/2]*int(c))
            pattern.extend([0]*int(c)) # 0 is file

        if i % 2 != 0:
            pattern.extend([1]*int(c)) # 1 is space

r_nums = list(reversed(nums))

total = 0
nums_count = 0
r_nums_count = 0

for i, p in enumerate(pattern):
    if i < len(nums):
        if p == 0:
            total += i * nums[nums_count]
            nums_count += 1
        if p == 1:
            total += i * r_nums[r_nums_count]
            r_nums_count += 1
    else:
        break

print(total)