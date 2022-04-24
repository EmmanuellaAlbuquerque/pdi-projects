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
# filename = os.path.join('', 'julian.jpg')
# filename = os.path.join('', 'sobel.png')
# filename = os.path.join('', '20191126093552.jpg')
# filename = os.path.join('', 'chimney.png')
filename = os.path.join('', 'apple.png')

image = io.imread(filename)

# image = np.array([[[16, 16, 16],
#                    [20, 20, 20],
#                    [10, 10, 10]],

#                   [[4, 4, 4],
#                    [4, 4, 4],
#                    [4, 4, 4]],

#                   [[2, 2, 2],
#                    [8, 8, 8],
#                    [5, 5, 5]]])

if (len(image.shape) != 3):
    print('Binary image')
    image = color.gray2rgb(image)


sobel_mask_horizontal = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

sobel_mask_vertical = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

# Filtro Box
box_mask = np.array([[1/9]*3]*3)
# box_mask = np.array([[1/16]*4]*4)
# box_mask = np.array([[1/25]*5]*5)
# box_mask = np.array([[1/49]*7]*7)
# box_mask = np.array([[1/225]*15]*15)
# box_mask = np.array([[1/2401]*49]*49)

mask = box_mask


m = mask.shape[0]
n = mask.shape[1]

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

            neighborhood_list = []

            R_neighborhood = []
            G_neighborhood = []
            B_neighborhood = []
            for row in range(-initial_i, initial_i+1, 1):
                for column in range(-initial_j, initial_j+1, 1):

                    pixel_rgb = image[i+row][j+column]
                    [R, G, B] = pixel_rgb

                    R_neighborhood.append(R)
                    G_neighborhood.append(G)
                    B_neighborhood.append(B)

            g.append(
                [round(np.median(R_neighborhood)),
                 round(np.median(G_neighborhood)),
                 round(np.median(B_neighborhood))
                 ])

        except IndexError:
            # print('> sem extensão por zero.')
            continue

        except BaseException as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise


print(image.shape)

try:
    g_array = np.empty([num_rows - 2*initial_i, num_columns - 2*initial_j, 3])
except ValueError:
    print('Máscara maior que a imagem! v = ',
          image.shape, 'mask = ', mask.shape)
    exit()

# print(g)
# print(len(g))
print(g_array.shape)

k = 0
for i in range(g_array.shape[0]):
    for j in range(g_array.shape[1]):
        # print(i, j, k)
        g_array[i][j] = g[k]
        k += 1


# Exibindo os resultados
show_result_plot({
    "Original Image": image,
    # "Box Filter Image": g_array.astype(np.uint8)
    "Median Filter Image": g_array.astype(np.uint8)
})
