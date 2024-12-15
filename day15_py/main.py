import numpy as np

def translate_instruction(instruction):
    
    if instruction == '<':
        return (0, -1)
    if instruction == '^':
        return (-1, 0)
    if instruction == '>':
        return (0, 1)
    if instruction == 'v':
        return (1, 0)

def calc_new_position(curr, direction):
    return (curr[0] + direction[0], curr[1] + direction[1])

def move_agent(arr, position, direction, moves):

    if arr[position] == 5:
        return moves
    
    if arr[position] == 0:
        moves[0] = position
        return moves
    
    if arr[position] == 1:
        position = calc_new_position(position, direction)
        moves[1] = position
        moves = move_agent(arr, position, direction, moves)
        if 0 not in moves.keys():
            return {}
        else:
            return moves

f = open('input.txt', 'r')

arr_ls = []
dirs = []

for line in f:
    line_ls = []
    for char in line:
        if char == '#':
            line_ls.append(5)
        if char == '.':
            line_ls.append(0)
        if char == 'O':
            line_ls.append(1)
        if char == '@':
            line_ls.append(2)
        if char in ['<', '^', '>', 'v']:
            dirs.append(char)
    if line_ls != []:
        arr_ls.append(line_ls)

arr = np.array(arr_ls)

for d in dirs:
    direction = translate_instruction(d)
    current_position = np.argwhere(arr == 2)[0]
    new_position = calc_new_position(current_position, direction)
    agent_move = new_position
    agent_position = (current_position[0], current_position[1])

    moves = {}
    moves = move_agent(arr, new_position, direction, moves)
    # print(d)
    # print(moves)
    # print(agent_move)
    # print(agent_position)
    
    if moves == {}:
        print("Not moving")
    else:
        arr[agent_move] = 2
        arr[agent_position] = 0
        if 1 in moves.keys():
            arr[moves[1]] = 1

    # print(arr)

crate_positions = np.where(arr == 1)
total = 0

for y in range(len(crate_positions[0])):
    total += crate_positions[0][y] * 100 + crate_positions[1][y]

print(total)


# RULES:
# If is wall -> don't move
# If is 0 -> move agent
    # current position, new position
# If is box -> check next -> If is 0 -> move agent and box
    # Move box into free, move agent into box
    # Need original position, new box position
# If is box -> check next -> if is 5 -> don't move
