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

print(b_a_np)

total = 0

for i in range(b_a_np.shape[0]): # Solve using lin regression
    A = (res_np[i][0]*b_b_np[i][1] - res_np[i][1]*b_b_np[i][0]) / (b_a_np[i][0]*b_b_np[i][1] - b_a_np[i][1]*b_b_np[i][0])
    B = (b_a_np[i][0]*res_np[i][1] - b_a_np[i][1]*res_np[i][0]) / (b_a_np[i][0]*b_b_np[i][1] - b_a_np[i][1]*b_b_np[i][0])
    
    if A.is_integer() and B.is_integer():
        to_append = (A*3) + B
        total += to_append

print(total)