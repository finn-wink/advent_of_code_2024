import numpy as np

def mix_and_prune(num, num2):

    mixed = num ^ num2
    pruned = mixed % 16777216

    return pruned

def get_last_digit(digit):
    return int(str(digit)[-1])

def list_to_string(this_list):
    return ','.join(map(str, this_list))

f = open('input.txt', 'r')

search_nums = []

for line in f:
    search_nums.append(int(line.strip()))

all_numbers = []
full_secret = 0

for num in search_nums:
    seller = []
    for i in range(2000):
        if i != 0:
            num = step3
        else:
            seller.append(num)    
        step1 = mix_and_prune(num, num*64)
        step2 = mix_and_prune(step1, step1//32)
        step3 = mix_and_prune(step2, step2*2048)
        seller.append(step3)
    
    all_numbers.append(seller)

last_digit = []

# Only extract the last digit of the int
for sellers in all_numbers:
    last_digit.append(list(map(get_last_digit, sellers)))

subtract_list = []

for sss in last_digit:
    sub2 = [0] + sss[:-1]
    sub2_np = np.array(sub2)
    sss_np = np.array(sss)
    diff = sss_np - sub2_np
    diff_l = diff.tolist()
    subtract_list.append(diff_l)

all_banana_dict = {}

for j, pattern in enumerate(subtract_list):
    banana_dict = {}
    for i, row in enumerate(pattern):
        if i > 2:
            if list_to_string(pattern[i-3:i+1]) not in banana_dict.keys():
                banana_dict[list_to_string(pattern[i-3:i+1])] = last_digit[j][i]
    
    for key, val in banana_dict.items():
        if key not in all_banana_dict.keys():
            all_banana_dict[key] = val
        else:
            all_banana_dict[key] += val

sorted_bananas = dict(sorted(all_banana_dict.items(), key=lambda item: item[1]))

print(sorted_bananas)



# Find the last digit of all that are generated
# Make same index as array of differences
# Find the 4 number sequence that leads to the highest number of bananas
# Find the highest numbers
# Find the sequences 4 beforehand (np.where)
# Compare to see which sequences lead to the highest numbers

# Find only the first occurences of the sequences