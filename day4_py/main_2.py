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

PATTERN1 = np.array([[M,-1,M], [-1,A,-1], [S,-1,S]])
PATTERN2 = np.rot90(PATTERN1)
PATTERN3 = np.rot90(PATTERN2)
PATTERN4 = np.rot90(PATTERN3)

MASK1 = PATTERN1 != -1
MASK2 = np.rot90(MASK1)
MASK3 = np.rot90(MASK2)
MASK4 = np.rot90(MASK3)

count = 0

for row in range(m_orig.shape[0]):
    for col in range(m_orig.shape[1]):
        slice_ = m_orig[row:row+3,col:col+3]
        if slice_.shape == (3,3):
            if np.all(slice_[MASK1] == PATTERN1[MASK1]) or np.all(slice_[MASK2] == PATTERN2[MASK2]) or np.all(slice_[MASK3] == PATTERN3[MASK3]) or np.all(slice_[MASK4] == PATTERN4[MASK4]):
                count += 1

print(count)