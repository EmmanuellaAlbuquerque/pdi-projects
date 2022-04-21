import numpy as np
import os
from skimage import io, data, color
from dimgprocessing_module import show_result_plot

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

            # print('V(i,j) = ', v[i][j])

            R_correlation_sum = 0
            G_correlation_sum = 0
            B_correlation_sum = 0
            for i in range(v.shape[0]):
                # print("v:\n", v[i], "\n")
                # print("box_mask:\n", box_mask[i], "\n")

                R_band_V = np.empty([len(v[i])])
                R_band_V.fill(-1)

                G_band_V = np.empty([len(v[i])])
                G_band_V.fill(-1)

                B_band_V = np.empty([len(v[i])])
                B_band_V.fill(-1)

                for pixel in range(len(v[i])):
                    # print('pixel:', pixel)

                    R_band_V[pixel] = v[i][pixel][0]
                    G_band_V[pixel] = v[i][pixel][1]
                    B_band_V[pixel] = v[i][pixel][2]

                # print(R_band_V)
                # print(G_band_V)
                # print(B_band_V)
                R_correlation_sum += np.inner(R_band_V, box_mask[i])
                G_correlation_sum += np.inner(G_band_V, box_mask[i])
                B_correlation_sum += np.inner(B_band_V, box_mask[i])

            # print(g[i][j])
            # g[i][j] = [R_correlation_sum, G_correlation_sum, B_correlation_sum]
            g.append([round(R_correlation_sum), round(
                G_correlation_sum), round(B_correlation_sum)])
            # print(g[i][j])

        except:
            # print('> sem extensão por zero.')
            f = 1


print(image.shape)

g_array = np.empty([num_rows - 2*initial_i, num_columns - 2*initial_j, 3])
# print(g_array)
# print(g.shape)
print(g_array.shape)

k = 0
for i in range(g_array.shape[0]):
    for j in range(g_array.shape[1]):
        g_array[i][j] = g[k]
        k += 1

# print(g_array)

for i in range(3):
    for j in range(3):
        print('Image =>', image[i][j])

print('G =>', g_array[0][0])

# Exibindo os resultados
# show_result_plot({
#     "Original Image": image,
#     "Box Filter Image": g_array.astype(np.uint8)
# })

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
