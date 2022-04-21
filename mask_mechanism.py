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

for i in range(initial_i, image.shape[0]):
    for j in range(initial_j, image.shape[1]):

        try:
            # Vizinhança v(i,j)
            v = np.array([
                [image[i-1][j-1], image[i-1][j], image[i-1][j+1]],
                [image[i][j-1], image[i][j], image[i][j+1]],
                [image[i+1][j-1], image[i+1][j], image[i+1][j+1]]
            ])

            print(v)

            print('V(i,j) = ', v[i][j])

        except:

            print('________________________________')
