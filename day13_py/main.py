import numpy as np

# def evaluate(button_a, button_b, result, presses):


f = open('input.txt', 'r')

b_a = []
b_b = []
res = []

for line in f:
    if line == '\n':
        continue
    line = line.strip('\n')
    coord_str = line[line.find('X'):]
    cords = coord_str.split(',')

    if 'Button A:' in line:  
        b_a.append([int(cords[0].strip('X').strip('+')), int(cords[1].strip().strip('Y').strip('+'))])
    if 'Button B:' in line:
        b_b.append([int(cords[0].strip('X').strip('+')), int(cords[1].strip().strip('Y').strip('+'))])
    if 'Prize' in line:
        res.append([int(cords[0].strip('X').strip('=')), int(cords[1].strip().strip('Y').strip('='))])

b_a_np = np.array(b_a)
b_b_np = np.array(b_b)
res_np = np.array(res)
res_np = res_np + 10000000000000

# print(b_a_np)
# print(b_b_np)
# print(res_np)

tokens = []

for i in range(b_a_np.shape[0]):

    bigger_a = max([b_a_np[i][0], b_b_np[i][0]])
    smaller_a = min([b_a_np[i][0], b_b_np[i][0]])
    bigger_b = max([b_a_np[i][1], b_b_np[i][1]])
    smaller_b = min([b_a_np[i][1], b_b_np[i][1]])

    max_all = max([round(res_np[i][0] / smaller_a), round(res_np[i][1] / smaller_b)]) + 1
    min_all = min([round(res_np[i][0] / bigger_a), round(res_np[i][1] / bigger_b)]) - 1

    # minimum taps result/bigger number
    # maximum taps result/smalle number
    # whichever is bigger or smaller -> use
    _result = []
    for mult in np.arange(start=min_all, stop=max_all + 1):
        for mult2 in np.arange(start=1, stop=101):
            resultx = b_a_np[i][0] * mult
            resulty = b_a_np[i][1] * mult
            resultx1 = b_b_np[i][0] * mult2
            resulty1 = b_b_np[i][1] * mult2

            if resultx + resultx1 == res_np[i][0] and resulty + resulty1 == res_np[i][1]:
                _result.append(mult * 3 + mult2 * 1)
    if _result != []:
        tokens.append(min(_result))

total = 0

for t in tokens:
    total += t

print(total)