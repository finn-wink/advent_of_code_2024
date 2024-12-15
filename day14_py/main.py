import numpy as np
np.set_printoptions(threshold=np.inf)

f = open('input.txt', 'r')

positions = []
velocities = []

for line in f:
    for x, _t in enumerate(line.split(sep=' ')):
        if '\n' in _t:
            _t = _t[:-1]
        _c = _t[2:]
        pos = _c.split(sep=',')
        if 'p' in _t:
            positions.append([int(pos[0]), int(pos[1])])
        if 'v' in _t:
            velocities.append([int(pos[0]), int(pos[1])])

pos_arr = np.array(positions)
vec_arr = np.array(velocities)

seconds = 1000

max_x = 101
max_y = 103


for i in range(seconds):
    for cur, pos in enumerate(pos_arr):
        x1 = pos_arr[cur][0] + vec_arr[cur][0]
        y1 = pos_arr[cur][1] + vec_arr[cur][1]

        if x1 < 0:
            x1 = x1 + max_x
        if y1 < 0:
            y1 = y1 + max_y
        if x1 >= max_x:
            x1 = x1 - max_x
        if y1 >= max_y:
            y1 = y1 - max_y

        pos_arr[cur][0] = x1
        pos_arr[cur][1] = y1

# Plot the graph
graph = np.zeros((103,101))

for x, y in pos_arr:
    graph[y,x] = 1

print(graph)



# center_x = max_x // 2
# center_y = max_y // 2
# q1 = 0
# q2 = 0
# q3 = 0
# q4 = 0

# for p in pos_arr:
#     if p[0] == center_x or p[1] == center_y:
#         continue
#     elif p[0] < center_x:
#         if p[1] < center_y:
#             q1 += 1
#         else:
#             q3 += 1
#             print(p)
#     else:
#         if p[1] < center_y:
#             q2 += 1
#         else:
#             q4 += 1

# print([q1,q2,q3,q4])

# print(q1 * q2 * q3 * q4)