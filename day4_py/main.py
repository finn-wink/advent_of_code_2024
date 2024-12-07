import numpy as np

X = 0
M = 1
A = 2
S = 3

biglist = []

f = open('input.txt', 'r')
for x in f:
    list1 = []
    for c in x:
        if c == 'X':
            list1.append(X)
        elif c == 'M':
            list1.append(M)
        elif c == 'A':
            list1.append(A)
        elif c == 'S':
            list1.append(S)

    biglist.append(list1)
        
m_orig = np.array(biglist)
m_90 = np.rot90(m_orig)

def count_diagonal(array):
    """
    Makes a diagonal from a numpy array and counts XMAS | SAMX occurences. 
    """
    count_diag = 0

    for i in range(len(array)-1):
        diag = np.diagonal(array, offset=i)
        diag_2 = np.diagonal(array, offset=-i)
        if i != 0:
            diag_matrix = np.array([diag, diag_2])
        else:
            diag_matrix = np.array([diag])
            print(diag_matrix.shape)

        count_diag += find_pattern(diag_matrix)

    return count_diag    


def find_pattern(array):
    
    count = 0
    PATTERN = np.array([0,1,2,3])
    PATTERN_R = np.flip(PATTERN)

    for row in array:
        for index, col in enumerate(row):
            slice_ = row[index:index+4]
            if np.array_equal(slice_, PATTERN) or np.array_equal(slice_, PATTERN_R):
                count += 1

    return count

c1 = find_pattern(m_orig)
c2 = find_pattern(m_90)
c3 = count_diagonal(m_orig)
c4 = count_diagonal(m_90)

full_count = c1 + c2 + c3 + c4

print(full_count)