import numpy as np

def check_order(order):
    breaker = False
    for i, num in enumerate(order):
        # print(num)
        if num not in rulebook.keys():
            print('Number not found')
            breaker = True

        if breaker:
            break

        slice_before = order[0:i]
        if i != 0:
            for slice_num in slice_before:
                if slice_num not in rulebook[num]['before']:
                    breaker = True
                    break

        slice_after = order[i+1:]
        if i < len(order) - 1:
            for slice_num in slice_after:
                if slice_num not in rulebook[num]['after']:
                    breaker = True
                    break

    if breaker == False:
        return True
    else:
        return False

def reorder(order):
    correct_order = []
    other_nums = order.copy()
    while set(correct_order) != set(order):
        for num in order:
            for other_num in other_nums:
                if other_num not in rulebook[num]['after']:
                    if other_num == num:
                        continue
                    other_num = None
                    break
            if other_num:
                if num not in correct_order:
                    correct_order.append(num)
                other_nums = np.setdiff1d(other_nums, np.array([num]))

    print(correct_order)

    return correct_order

rulebook = {}
middle_count = 0

f = open('input.txt', 'r')
for line in f:
    if '|' in line:
        first_num = int(line[0:2])
        second_num = int(line[-3:-1])

        if first_num not in rulebook.keys():
            rulebook[first_num] = {
                'before': [],
                'after': []
            }
        if second_num not in rulebook.keys():
            rulebook[second_num] = {
                'before': [],
                'after': []
            }
        
        rulebook[first_num]['after'].append(second_num)
        rulebook[second_num]['before'].append(first_num)

    # print(rulebook.keys())

    if ',' in line:
        order = np.fromstring(line, dtype=int, sep=',')
        
        if not check_order(order):
            order = reorder(order)

            # print('Reordered')
    
            middle_count += order[int(len(order)//2)]
        # else:
            # print('Line already good')

        # if not breaker:
        #     middle_count += order[int(len(order)//2)]

print(middle_count)