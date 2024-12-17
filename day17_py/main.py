import numpy as np

f = open('input.txt', 'r')

registers = {}

# first number opcode -> operand, number after it

for i, line in enumerate(f):
    if 'Register' in line:
        if i == 0:
            registers['a'] = int(line[12:].strip())
        if i == 1:
            registers['b'] = int(line[12:].strip())
        if i == 2:
            registers['c'] = int(line[12:].strip())

    if 'Program' in line:
        ind = line.find(':') + 1
        program = line[ind:].strip().split(',')

program = list(map(int, program))

def literal_operand(value):
    return value

def combo_operand(value, registers):

    if value < 4:
        return value
    if value == 4:
        return registers['a']
    if value == 5:
        return registers['b']
    if value == 6:
        return registers['c']
    if value == 7:
        print("BROKEN")
        raise RuntimeError

def opcode_0(operand, registers):
    combo = combo_operand(operand, registers)
    registers['a'] = registers['a']//2**combo

def opcode_1(operand, registers):
    registers['b'] = registers['b'] ^ operand

def opcode_2(operand, registers):
    combo = combo_operand(operand, registers)
    registers['b'] = combo % 8 

def opcode_3(operand, registers):
    if registers['a'] == 0:
        return 100
    else:
        return operand # Set the pointer to this
    
def opcode_4(registers):
    registers['b'] = registers['b'] ^ registers['c']

def opcode_5(operand, registers):
    combo = combo_operand(operand, registers)
    out = combo % 8
    return out # Will be added to the output with , between

def opcode_6(operand, registers):
    combo = combo_operand(operand, registers)
    registers['b'] = registers['a']//2**combo

def opcode_7(operand, registers):
    combo = combo_operand(operand, registers)
    registers['c'] = registers['a']//2**combo

def generate_indeces(start_list, length_list):
    new_ind = [start_list + 2 * i for i in range(int((length_list - start_list)/2))]
    return new_ind

solved = False

start_list = 0
length_list = len(program)
output = []
count = 0
breaker = False

while not solved:

    indeces = generate_indeces(start_list, length_list)
    halt = max(indeces)

    for x in indeces:
        # print('x ' + str(x))
        if program[x] == 0:
            opcode_0(program[x+1], registers)
        
        if program[x] == 1:
            opcode_1(program[x+1], registers)
        
        if program[x] == 2:
            opcode_2(program[x+1], registers)
        
        if program[x] == 3:
            index = opcode_3(program[x+1], registers)

            if index == 100:
                print("didn't get em")
            
            else:
                start_list = index
                # print("Gottem")
                break
        
        if program[x] == 4:
            register_b = opcode_4(registers)
        
        if program[x] == 5:
            res = opcode_5(program[x+1], registers)
            output.append(res)
        
        if program[x] == 6:
            opcode_6(program[x+1], registers)

        if program[x] == 7:
            opcode_7(program[x+1], registers)

        if x == halt:
            breaker = True
            break
        
        count += 1

    if breaker:
        break

print(output)
print(count)


# Need a function that generates list of indices
# according to length of the list and the start

# While unsolved, run for loop, if 3, call function for new list
# and break loop
