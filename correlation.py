from tracemalloc import stop
import numpy as np
import os
from skimage import io, data, color
from dimgprocessing_module import show_result_plot
import sys

# Carregando imagem de entrada
# filename = os.path.join('', 'black-line-center.png')
# filename = os.path.join('', 'yiq-test.png')
# filename = os.path.join('', 'correlation_test.png')
filename = os.path.join('', 'julian.jpg')
image = io.imread(filename)

if (len(image.shape) != 3):
    print('Binary image')
    image = color.gray2rgb(image)

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
# box_mask = np.array([[1/9]*3]*3)
# box_mask = np.array([[1/25]*5]*5)
# box_mask = np.array([[1/49]*7]*7)
# box_mask = np.array([[1/225]*15]*15)
box_mask = np.array([[1/2401]*49]*49)

mask = box_mask

# print(box_mask)
# print(box_mask.shape)
# exit()

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
            # v = np.array([
            #     [image[i-1][j-1], image[i-1][j], image[i-1][j+1]],
            #     [image[i][j-1], image[i][j], image[i][j+1]],
            #     [image[i+1][j-1], image[i+1][j], image[i+1][j+1]]
            # ])
            # v = np.array([
            #     [image[i-2][j-2], image[i-2][j-1], image[i-2]
            #         [j], image[i-2][j+1], image[i-2][j+2]],
            #     [image[i-1][j-2], image[i-1][j-1], image[i-1]
            #         [j], image[i-1][j+1], image[i-1][j+2]],
            #     [image[i][j-2], image[i][j-1], image[i]
            #         [j], image[i][j+1], image[i][j+2]],
            #     [image[i+1][j-2], image[i+1][j-1], image[i+1]
            #         [j], image[i+1][j+1], image[i+1][j+2]],
            #     [image[i+2][j-2], image[i+2][j-1], image[i+2]
            #         [j], image[i+2][j+1], image[i+2][j+2]]
            # ])
            neighborhood_list = []
            for row in range(-initial_i, initial_i+1, 1):
                for column in range(-initial_j, initial_j+1, 1):

                    # print('i, j:', row, column)
                    neighborhood_list.append(image[i+row][j+column])

            # print(i, j, len(neighborhood_list))

            rows = mask.shape[0]
            columns = mask.shape[1]

            v = np.empty([rows, columns, 3])
            # print(v.shape)

            k = 0
            for q in range(v.shape[0]):
                for w in range(v.shape[1]):

                    v[q][w] = neighborhood_list[k]
                    k += 1

            # print('V:', v)
            # print('v-shape:', v.shape)

            # print('V(i,j) = ', v[i][j])

            R_correlation_sum = 0
            G_correlation_sum = 0
            B_correlation_sum = 0
            for v_index in range(v.shape[0]):
                # print("v:\n", v[i], "\n")
                # print("box_mask:\n", box_mask[i], "\n")

                R_band_V = np.empty([len(v[v_index])])
                R_band_V.fill(-1)

                G_band_V = np.empty([len(v[v_index])])
                G_band_V.fill(-1)

                B_band_V = np.empty([len(v[v_index])])
                B_band_V.fill(-1)

                # print(len(v[v_index]))
                for pixel in range(len(v[v_index])):
                    # print('pixel:', pixel)

                    R_band_V[pixel] = v[v_index][pixel][0]
                    G_band_V[pixel] = v[v_index][pixel][1]
                    B_band_V[pixel] = v[v_index][pixel][2]

                # print(R_band_V)
                # print(G_band_V)
                # print(B_band_V)
                R_correlation_sum += np.inner(R_band_V, box_mask[v_index])
                G_correlation_sum += np.inner(G_band_V, box_mask[v_index])
                B_correlation_sum += np.inner(B_band_V, box_mask[v_index])

            # print(g[i][j])
            # g[i][j] = [R_correlation_sum, G_correlation_sum, B_correlation_sum]
            g.append([round(R_correlation_sum), round(
                G_correlation_sum), round(B_correlation_sum)])

        except IndexError:
            # print('> sem extensão por zero.')
            continue

        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise


print(image.shape)

g_array = np.empty([num_rows - 2*initial_i, num_columns - 2*initial_j, 3])
# print(g)
# print(len(g))
print(g_array.shape)

k = 0
for i in range(g_array.shape[0]):
    for j in range(g_array.shape[1]):
        # print(i, j, k)
        g_array[i][j] = g[k]
        k += 1

# print(g_array)

# for i in range(3):
#     for j in range(3):
#         print('Image =>', image[i][j])

# print('G =>', g_array[g_array.shape[0] - 1][g_array.shape[1] - 1])

# Exibindo os resultados
show_result_plot({
    "Original Image": image,
    "Box Filter Image": g_array.astype(np.uint8)
})

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
