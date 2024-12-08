import numpy as np

def is_coord_inside(coords, m_orig):
    if coords[0] >= 0 and coords[0] < m_orig.shape[1] and coords[1] >=0 and coords[1] < m_orig.shape[1]:
        return True


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

hash_list = []

for sym in all_symbols.values():
    
    if sym == all_symbols['.']:
        continue
    
    coords = np.where(m_orig == sym)
    coords = list(zip(*coords))
    coords_ind = np.arange(len(coords))
    print(coords_ind)
    comb_array = np.array(np.meshgrid(coords_ind, coords_ind)).T.reshape(-1, 2) 
    
    for i in comb_array:
        
        coord1 = coords[i[0]]
        coord2 = coords[i[1]]

        if coord1 != coord2:
            print(coord1, coord2)
            dist_y = coord1[0] - coord2[0]
            dist_x = coord1[1] - coord2[1]
            print([dist_y, dist_x])
            
            hash1_y = coord1[0] + dist_y 
            hash1_x = coord1[1] + dist_x 

            hash2_y = coord2[0] + dist_y * -1
            hash2_x = coord2[1] + dist_x * -1

            if is_coord_inside([hash1_y, hash1_x], m_orig):
                if [hash1_y, hash1_x] not in hash_list:
                    hash_list.append([hash1_y, hash1_x])

            if is_coord_inside([hash2_y, hash2_x], m_orig):
                if [hash2_y, hash2_x] not in hash_list:
                    hash_list.append([hash2_y, hash2_x])

print(len(hash_list))

# diff list
# check if diffs on either side are in the square
