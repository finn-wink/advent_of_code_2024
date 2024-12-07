import re

f = open('input.txt', 'r')

all_str = ''

for x in f:
    all_str += x

all_str = all_str.replace('\n', '').replace(' ', '')

# all_str_l = all_str.split(sep="don't()")

total = 0

first = re.split(r"don't\(\)", all_str, maxsplit=1)[0]
pattern = r"do\(\)(.*?)don't\(\)"
matches = re.findall(pattern, all_str, re.DOTALL)

matches.append(first)
all_str_l = matches

for x in all_str_l:
    # new_l = x.split(sep='do()')
    # print(new_l)
    # if len(new_l) != 1:
    #     new_l = new_l[1:]
    # elif new_l[0] == x[0]:
    #     continue
    # for line in new_l:
        # print(line)
    patt = re.findall(r"mul\(\s*[0-9]{1,3}\s*,\s*[0-9]{1,3}\s*\)", x)
    # print(matches)
    for match in patt:
        numbers = match[4:-1].split(',')
        result = int(numbers[0]) * int(numbers[1])
        total += result

print(total)
