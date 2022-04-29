# Digital Image Processing Functions Module
# dimgprocessing-module.py

from skimage import io, data, color
from matplotlib import pyplot as plt
import numpy as np
from colorama import Fore, Style


def RGBtoYIQ(original_image, mode='yiq'):
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

            # for Y test
            if (mode == 'y'):
                print('Usar somente em propósito de testes da banda Y.')
                yiq_image[i][j] = [Y, Y, Y]
                yiq_image = yiq_image.astype(np.uint8)

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

            rgb_image[i][j] = [np.round(R), np.round(G), np.round(B)]

            rgb_image[i][j] = np.clip(rgb_image[i][j], 0, 255)

    return rgb_image.astype(np.uint8)


def negative(original_image, mode='rgb'):
    """Filtro para interver a cor, isto é, gerar o
       negativo das imagens.

    Args:
        original_image (ndarray): o array da imagem de entrada.

    Returns:
        ndarray : o array com as bandas invertidas.
    """

    L = pow(2, 8)  # 256

    if (mode == 'yiq'):
        print('Gerando Negativo somente na banda Y.')

        num_rows = original_image.shape[0]
        num_columns = original_image.shape[1]

        yiq_negative_image = np.empty([num_rows, num_columns, 3])

        for i in range(num_rows):
            for j in range(num_columns):

                [Y, I, Q] = original_image[i][j]

                Y_final = (L - 1) - Y

                yiq_negative_image[i][j] = [Y_final, I, Q]

        return yiq_negative_image

    negative_image = (L - 1) - original_image

    return negative_image


def show_result_plot(images_dict):

    number_of_images = len(images_dict)
    n_row, n_col = 1, number_of_images

    # PLOT CONFIG
    fig, axs = plt.subplots(
        n_row, n_col, constrained_layout=True)

    if (type(axs) != np.ndarray):
        print(
            f'{Fore.RED}ALERT:{Style.RESET_ALL}'
            ' Exiba pelo menos 2 images (a original e a de saída)'
            ' para visualizar os resultados.')
        exit()

    images_names_list = list(images_dict.keys())

    for i in range(number_of_images):
        image_name = images_names_list[i]
        matrix = images_dict[image_name]

        axs[i].set_title(image_name)
        axs[i].imshow(matrix)

    fig.canvas.manager.set_window_title('Results')
    plt.show()
