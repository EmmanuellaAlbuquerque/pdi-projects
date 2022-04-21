import numpy as np
import os
from skimage import io, data, color

# Carregando imagem de entrada
filename = os.path.join('', 'correlation_test.png')
image = io.imread(filename)

# print(original_image.shape)

# image = np.array([[[249, 249, 249],
#                    [249, 249, 249],
#                    [249, 249, 249]],

#                   [[5, 5, 5],
#                    [249, 249, 249],
#                    [249, 249, 249]],

#                   [[249, 249, 249],
#                    [249, 249, 249],
#                    [249, 249, 249]]])

# print(image.shape)

# image = np.array([[[5, 5, 1],
#                    [2, 2, 1],
#                    [3, 3, 1]],

#                   [[10, 10, 2],
#                    [20, 20, 2],
#                    [30, 30, 2]],

#                   [[100, 100, 3],
#                    [200, 200, 3],
#                    [300, 300, 3]]])

# image = np.array([
#     [249, 249, 249],
#     [5, 249, 249],
#     [249, 249, 249]
# ])

# Filtro Box
box_mask = np.array([
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9],
    [1/9, 1/9, 1/9]
])

m = box_mask.shape[0]
n = box_mask.shape[1]

# A máscara desliza sobre a imagem de entrada

# Calculando a posição do pixel central para aplicar a máscara
initial_i = int((m - 1)/2)
initial_j = int((n - 1)/2)

# print(initial_i, initial_j)
# print(image.shape[0], image.shape[1])

# - primeira linha - ultima linha
num_rows = image.shape[0]
num_columns = image.shape[1]
# g = np.empty([num_rows, num_columns])
g = np.empty([num_rows, num_columns, 3])
g.fill(-1)
# print(g)

for i in range(initial_i, image.shape[0]):
    for j in range(initial_j, image.shape[1]):

        # print('( ' + str(i-1), ',', str(j-1), ')', '=>', image[i-1][j-1])
        # print('( ' + str(i-1), ',', str(j), ')', '=>', image[i-1][j])
        # print('( ' + str(i-1), ',', str(j+1), ')', '=>', image[i-1][j+1])
        # print('( ' + str(i), ',', str(j-1), ')', '=>', image[i][j-1])
        # print('( ' + str(i), ',', str(j), ')', '=>', image[i][j])
        # print('( ' + str(i), ',', str(j+1), ')', '=>', image[i][j+1])
        # print('( ' + str(i+1), ',', str(j-1), ')', '=>', image[i+1][j-1])
        # print('( ' + str(i+1), ',', str(j), ')', '=>', image[i+1][j])
        # print('( ' + str(i+1), ',', str(j+1), ')', '=>', image[i+1][j+1])

        # print('( ' + str(i-1), ',', str(j-1), ')')
        # print('( ' + str(i-1), ',', str(j), ')')
        # print('( ' + str(i-1), ',', str(j+1), ')')
        # print('( ' + str(i), ',', str(j-1), ')')
        # print('( ' + str(i), ',', str(j), ')')
        # print('( ' + str(i), ',', str(j+1), ')')
        # print('( ' + str(i+1), ',', str(j-1), ')')
        # print('( ' + str(i+1), ',', str(j), ')')
        # print('( ' + str(i+1), ',', str(j+1), ')')

        try:
            # Vizinhança v(i,j)
            v = np.array([
                [image[i-1][j-1], image[i-1][j], image[i-1][j+1]],
                [image[i][j-1], image[i][j], image[i][j+1]],
                [image[i+1][j-1], image[i+1][j], image[i+1][j+1]]
            ])

            print(v)

            print('V(i,j) = ', v[i][j])

            R_correlation_sum = 0
            G_correlation_sum = 0
            B_correlation_sum = 0
            for i in range(v.shape[0]):
                print("v:\n", v[i], "\n")
                print("box_mask:\n", box_mask[i], "\n")

                R_band_V = np.empty([len(v[i])])
                R_band_V.fill(-1)

                G_band_V = np.empty([len(v[i])])
                G_band_V.fill(-1)

                B_band_V = np.empty([len(v[i])])
                B_band_V.fill(-1)

                for pixel in range(len(v[i])):
                    print('pixel:', pixel)

                    R_band_V[pixel] = v[i][pixel][0]
                    G_band_V[pixel] = v[i][pixel][1]
                    B_band_V[pixel] = v[i][pixel][2]

                print(R_band_V)
                print(G_band_V)
                print(B_band_V)
                R_correlation_sum += np.inner(R_band_V, box_mask[i])
                G_correlation_sum += np.inner(G_band_V, box_mask[i])
                B_correlation_sum += np.inner(B_band_V, box_mask[i])

            print(g[i][j])
            g[i][j] = [R_correlation_sum, G_correlation_sum, B_correlation_sum]
            print(g[i][j])

        except:
            g = g[g != -1]
            print('________________________________')
            print(g)

            exit()


# v = np.empty([m, n])

# Pixel a pixel da imagem de entrada
# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):

#         if (v.shape()[0] == m and v.shape()[1] == n):
#             print('Calculate Frobenius')
#             print(v)


# [image[i][j-1], image[i][j], image[i][j+1]],
#       [image[i+1][j-1], image[i+1][j], image[i+1][j+1]]

# Vizinhança v(i,j)
# v = np.array([
#     [image[i-1][j-1], image[i-1][j], image[i-1][j+1]],
#     [image[i][j-1], image[i][j], image[i][j+1]],
#     [image[i+1][j-1], image[i+1][j], image[i+1][j+1]]
# ])

# print(v)

# num_rows = image.shape[0]
# num_columns = image.shape[1]
# g = np.empty([num_rows, num_columns])

# g = np.empty([num_rows, num_columns, 3])
