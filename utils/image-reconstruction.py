# Reconstrução bilinear
# image-reconstruction.py

# f = (x, y)
from math import ceil
import numpy as np
from math import floor

# f = (10.5, 15.2)
# f = (0, 0.43)
# f = (0.43, 1.3)
f = (0.7, 1.3)

# image = np.array([[10, 20, 0],
#                   [30, 30, 25],
#                   [30, 30, 90]])

image = np.array([[7, 16, 1, 7],
                  [12, 7, 12, 16],
                  [12, 1, 7, 1]])

i = floor(f[0])
iplus1 = ceil(f[0])

j = floor(f[1])
jplus1 = ceil(f[1])

print(i, '< x <', iplus1)
print(j, '< y <', jplus1)

# image[i][j]
# print(i, j)
# print(i, jplus1)
# print(iplus1, j)
# print(iplus1, jplus1)

fij = image[i][j]
fi_jplus1 = image[i][jplus1]
fiplus1_j = image[iplus1][j]
fiplus1_jplus1 = image[iplus1][jplus1]

# fij = 10
# fi_jplus1 = 20
# fiplus1_j = 30
# fiplus1_jplus1 = 30

print('-----------------------')
print(fij)
print(fi_jplus1)
print(fiplus1_j)
print(fiplus1_jplus1)

fiy = fij + (f[1] - j) * (fi_jplus1 - fij)
fiplus1_y = fiplus1_j + (f[1] - j) * (fiplus1_jplus1 - fiplus1_j)
fxy = fiy + (f[0] - i) * (fiplus1_y - fiy)

print('-----------------------')
print(fiy)
print(fiplus1_y)
print(fxy, ' => ', round(fxy))
