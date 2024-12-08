import numpy as np

def is_coord_inside(coords, m_orig):
    if coords[0] >= 0 and coords[0] < m_orig.shape[0] and coords[1] >= 0 and coords[1] < m_orig.shape[1]:
        return True
    else:
        return False

def find_distance(coords):
    
    dist_y = coords[0][0] - coords[1][0]
    dist_x = coords[0][1] - coords[1][1]

    return (dist_y, dist_x)

def find_backward(coords, distance):
    
    hash1_y = coords[0] + distance[0]
    hash1_x = coords[1] + distance[1]

    return (hash1_y, hash1_x)

def find_forward(coords, distance):

    hash2_y = coords[0] + distance[0] * -1
    hash2_x = coords[1] + distance[1] * -1

    return (hash2_y, hash2_x)



f = open('input.txt', 'r')

all_symbols = {}
symbol_int = 0

for line in f:
    for unique in list(set(line)):
        if unique not in ['\n'] and unique not in all_symbols:
            all_symbols[unique] = symbol_int
            symbol_int += 1

r = open('input.txt', 'r')

bigList = []

for line in r:
    
    smallList = []
    
    for c in line:
        if c not in ['\n']:
            smallList.append(all_symbols[c])
    bigList.append(smallList)

m_orig = np.array(bigList)

antinodes = []
antennas = []

for sym in all_symbols.values():
    
    if sym == all_symbols['.']:
        continue
    
    coords = np.where(m_orig == sym)
    coords = list(zip(*coords))
    coords_ind = np.arange(len(coords))

    comb_array = np.array(np.meshgrid(coords_ind, coords_ind)).T.reshape(-1, 2) 
    
    for i in comb_array:
        
        coord1 = coords[i[0]]
        coord2 = coords[i[1]]
        
        if coord1 != coord2:
            
            check_forward = True
            check_backward = True
            
            distance = find_distance([coord1, coord2])

            search_coord1 = coord1
            search_coord2 = coord2

            while True:

                backward = find_backward(search_coord1, distance)
                forward = find_forward(search_coord2, distance)
                
                if check_forward:
                    if is_coord_inside(forward, m_orig):
                        if forward not in antinodes:
                            antinodes.append(forward)
                    else:
                        check_forward = False

                if check_backward:
                    if is_coord_inside(backward, m_orig):
                        if backward not in antinodes:
                            antinodes.append(backward)
                    else:
                        check_backward = False
                
                search_coord1 = backward
                search_coord2 = forward

                if not check_forward and not check_backward:
                    antennas.append(coord1)
                    antennas.append(coord2)
                    break

for ant in antennas: # Add antennas to antinodes
    if ant not in antinodes:
        antinodes.append(ant)

print(len(antinodes))