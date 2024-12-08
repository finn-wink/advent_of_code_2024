import itertools
import numpy as np

def calc_add(arg1, arg2):
    return arg1 + arg2

def calc_mul(arg1, arg2):
    return arg1 * arg2

def calc_conc(arg1, arg2):
    return int(str(arg1) + str(arg2))

def uniqe_arrays(length):
    all_combinations = list(itertools.product([0, 1, 2], repeat=length))

    np.random.shuffle(all_combinations)

    for combo in all_combinations:
        yield np.array(combo)

counter = 0

f = open('input.txt', 'r')
for x in f:
    goal = int(x.split(':')[0])
    args = x.split(':')[1]
    args = np.fromstring(args, dtype=int, sep=' ')

    for instructions in uniqe_arrays(len(args) - 1):

        result = 0
        for i, num in enumerate(args):
            if i == 0:
                result = num

            if i < len(args) - 1:
                if instructions[i] == 0:
                    result = calc_add(result, args[i+1])
                elif instructions[i] == 1:
                    result = calc_mul(result, args[i+1])
                else:
                    result = calc_conc(result, args[i+1])

        if result == goal:
            counter += result
            print(counter)
            break
