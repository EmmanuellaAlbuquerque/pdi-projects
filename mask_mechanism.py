# Mechanism to slide the mask

import numpy as np

image = np.array([
    [0, 0, 0, 0, 0],
    [0, 16, 20, 10, 0],
    [0, 4, 4, 4, 0],
    [0, 2, 8, 5, 0],
    [0, 0, 0, 0, 0]
])

box_mask = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

m = box_mask.shape[0]
n = box_mask.shape[1]

initial_i = int((m - 1)/2)
initial_j = int((n - 1)/2)


g = []

for i in range(initial_i, image.shape[0]):
    for j in range(initial_j, image.shape[1]):

        try:
            # Vizinhança v(i,j)
            v = np.array([
                [image[i-1][j-1], image[i-1][j], image[i-1][j+1]],
                [image[i][j-1], image[i][j], image[i][j+1]],
                [image[i+1][j-1], image[i+1][j], image[i+1][j+1]]
            ])

            print('V (', i, ',', j, ') =',
                  v[initial_i][initial_j])
            print(v)

            # g[i][j] = [v[initial_i][initial_j], 100, 100]
            g.append([v[initial_i][initial_j], 100, 100])

        except:

            print('> sem extensão por zero.')


print('------------------------')
# print(g.shape)
print(g)

num_rows = image.shape[0]
num_columns = image.shape[1]

g_array = np.empty([num_rows - 2*initial_i, num_columns - 2*initial_j, 3])
print(g_array)
print(g_array.shape)

k = 0
for i in range(g_array.shape[0]):
    for j in range(g_array.shape[1]):
        g_array[i][j] = g[k]
        k += 1


# Pixel a pixel da imagem de entrada
# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):

#         if (v.shape()[0] == m and v.shape()[1] == n):
#             print('Calculate Frobenius')
#             print(v)
