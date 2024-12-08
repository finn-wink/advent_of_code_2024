import numpy as np

biglist = []

f = open('input.txt', 'r')
for x in f:
    list1 = []
    for c in x:
        if c == '.':
            list1.append(0)
        if c == '#':
            list1.append(1)
        if c == '^':
            list1.append(2)
    biglist.append(list1)

m_orig = np.array(biglist)

def run_guard(m_orig):

    in_square = True    
    pos_visited = []
    cur_pos = [np.where(m_orig == 2)[0][0], np.where(m_orig == 2)[1][0]]

    while in_square:
        len_pos = len(pos_visited)
        while m_orig[cur_pos[0]-1,cur_pos[1]] != 1:
            if cur_pos not in pos_visited:
                pos_visited.append(cur_pos.copy())
            cur_pos = [cur_pos[0]-1,cur_pos[1]]
            if cur_pos[0] < 1:
                if cur_pos not in pos_visited:
                    pos_visited.append(cur_pos.copy())
                in_square = False
                break

        if in_square:
            while m_orig[cur_pos[0],cur_pos[1]+1] != 1:
                if cur_pos not in pos_visited:
                    pos_visited.append(cur_pos.copy())
                cur_pos = [cur_pos[0],cur_pos[1]+1]
                if cur_pos[1] >= m_orig.shape[1]-1:
                    if cur_pos not in pos_visited:
                        pos_visited.append(cur_pos.copy())
                    in_square = False
                    break

        if in_square:
            while m_orig[cur_pos[0]+1,cur_pos[1]] != 1:
                if cur_pos not in pos_visited:
                    pos_visited.append(cur_pos.copy())
                cur_pos = [cur_pos[0]+1,cur_pos[1]]
                if cur_pos[0] >= m_orig.shape[0]-1:
                    if cur_pos not in pos_visited:
                        pos_visited.append(cur_pos.copy())
                    in_square = False
                    break

        if in_square:
            while m_orig[cur_pos[0],cur_pos[1]-1] != 1:
                if cur_pos not in pos_visited:
                    pos_visited.append(cur_pos.copy())
                cur_pos = [cur_pos[0],cur_pos[1]-1]
                if cur_pos[1] < 1:
                    if cur_pos not in pos_visited:
                        pos_visited.append(cur_pos.copy())
                    in_square = False
                    break
    
        if len_pos == len(pos_visited):
            return []            

    return pos_visited

loop_count = 0

out = run_guard(m_orig)

for i, x in enumerate(out):
    if i == 0:
        continue

    m_orig[x[0], x[1]] = 1
    if len(run_guard(m_orig)) == 0:
        loop_count += 1

    m_orig[x[0], x[1]] = 0
print(loop_count)
    

