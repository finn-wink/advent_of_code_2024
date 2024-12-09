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

# For each group that is spaces -> check if any of the numbers groups are smaller or equal in length,
# if they are, append them to the new list first

# Check for each space if you can append numbers.
# Restart if the number changes by 1
# Append only if you have not reached the end of the loop and start again. 

print(nums)
print(pattern)