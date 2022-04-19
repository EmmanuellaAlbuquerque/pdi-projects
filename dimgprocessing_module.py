# Digital Image Processing Functions Module
# dimgprocessing-module.py

from skimage import io, data, color
from matplotlib import pyplot as plt
import numpy as np


def RGBtoYIQ(original_image):
    # print('Convertendo para o espaço de cores YIQ')

    num_rows = original_image.shape[0]
    num_columns = original_image.shape[1]

    yiq_image = np.empty([num_rows, num_columns, 3])

    for i in range(num_rows):
        for j in range(num_columns):

            [R, G, B] = original_image[i][j]

            # RGB para YIQ
            Y = 0.299*R + 0.587*G + 0.114*B
            I = 0.596*R - 0.274*G - 0.322*B
            Q = 0.211*R - 0.523*G + 0.312*B

            yiq_image[i][j] = [Y, I, Q]
            # print(I)
            # print("test:", yiq_image[i][j])

            # yiq_image[i][j] = [Y, Y, Y]
            # yiq_image[i][j] = [I, I, I]
            # yiq_image[i][j] = [Q, Q, Q]

            # print(R, G, B)
            # print(Y, I, Q)
            # exit()

    return yiq_image


def YIQtoRGB(original_image):
    # print('Convertendo para o espaço de cores YIQ')

    num_rows = original_image.shape[0]
    num_columns = original_image.shape[1]

    rgb_image = np.empty([num_rows, num_columns, 3])

    for i in range(num_rows):
        for j in range(num_columns):

            [Y, I, Q] = original_image[i][j]

            # YIQ para RGB
            R = 1.000*Y + 0.956*I + 0.621*Q
            G = 1.000*Y - 0.272*I - 0.647*Q
            B = 1.000*Y - 1.106*I + 1.703*Q

            R = round(R)
            G = round(G)
            B = round(B)

            rgb_image[i][j] = [R, G, B]

            # print(Y, I, Q)
            # print(R, G, B)

    return rgb_image.astype(np.uint8)


def negative(original_image):
    """Filtro para interver a cor, isto é, gerar o
       negativo das imagens.

    Args:
        original_image (ndarray): o array da imagem de entrada.

    Returns:
        ndarray : o array com as bandas invertidas.
    """

    L = pow(2, 8)  # 256
    negative_image = (L - 1) - original_image

    return negative_image


def show_result_plot(images_dict):

    number_of_images = len(images_dict)
    n_row, n_col = 1, number_of_images

    # PLOT CONFIG
    fig, axs = plt.subplots(
        n_row, n_col, constrained_layout=True)

    images_names_list = list(images_dict.keys())

    for i in range(number_of_images):
        image_name = images_names_list[i]
        matrix = images_dict[image_name]

        axs[i].set_title(image_name)
        axs[i].imshow(matrix)

    fig.canvas.manager.set_window_title('Results')
    plt.show()
