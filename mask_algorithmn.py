# Vizinhança

import numpy as np

image = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

print(image)

# mask = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ])

mask = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])

i, j = 3, 3
# v = np.array([
#     [image[i-2][j-2], image[i-2][j-1], image[i-2]
#      [j], image[i-2][j+1], image[i-2][j+2]],
#     [image[i-1][j-2], image[i-1][j-1], image[i-1]
#      [j], image[i-1][j+1], image[i-1][j+2]],
#     [image[i][j-2], image[i][j-1], image[i]
#      [j], image[i][j+1], image[i][j+2]],
#     [image[i+1][j-2], image[i+1][j-1], image[i+1]
#      [j], image[i+1][j+1], image[i+1][j+2]],
#     [image[i+2][j-2], image[i+2][j-1], image[i+2]
#      [j], image[i+2][j+1], image[i+2][j+2]]
# ])

# v = np.array([
#     [image[i-1][j-1], image[i-1][j], image[i-1][j+1]],
#     [image[i][j-1], image[i][j], image[i][j+1]],
#     [image[i+1][j-1], image[i+1][j], image[i+1][j+1]]
# ])

# print(v)


m = mask.shape[0]
n = mask.shape[1]

initial_i = int((m - 1)/2)
initial_j = int((n - 1)/2)

print('=>', i, j, image[i][j])


neighborhood_list = []
for row in range(-initial_i, initial_i+1, 1):
    for column in range(-initial_j, initial_j+1, 1):

        print('i, j:', row, column)
        neighborhood_list.append(image[i+row][j+column])

print(neighborhood_list)

num_rows = mask.shape[0]
num_columns = mask.shape[1]

g_array = np.empty([num_rows, num_columns])

k = 0
for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):
        g_array[i][j] = neighborhood_list[k]
        k += 1

print(g_array)
print(g_array.shape)
