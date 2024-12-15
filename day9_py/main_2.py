from itertools import groupby

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

r_nums = list(reversed(nums))

pattern = [list(group) for key, group in groupby(pattern)]
r_nums = [list(group) for key, group in groupby(r_nums)]

print(pattern)

for i, p in enumerate(pattern):
    if -1 in p:
        search_length = len(p)
        replace_element = 0
        for r_n in r_nums:
            if search_length >= len(r_n):
                for rr in r_n:
                    pattern[i][replace_element] = rr
                    replace_element += 1
                    search_length -= 1
                r_nums.remove(r_n)

print(pattern)

# Try to fill all the -1's using the reverse groups
# Delete the groups that are in there
# Replace 0s with the left over groups


g_nums = [list(group) for key, group in groupby(nums)]

num_index = 0

# print(nums)
# print(r_nums)
# print(pattern)