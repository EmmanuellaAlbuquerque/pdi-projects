from math import ceil
from skimage import io, data, color
from matplotlib import pyplot as plt
import os
import copy
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


def show_result_plot(original_image, negative_image, yiq_image, rgb_image):
    #  PLOT CONFIG: 1 row X 2 column
    n_row, n_col = 1, 4
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(
        n_row, n_col, constrained_layout=True)

    ax1.set_title('Original Image')
    ax1.imshow(original_image)

    ax2.set_title("Negative Image")
    ax2.imshow(negative_image)

    ax3.set_title("YIQ Image")
    ax3.imshow(yiq_image)

    ax4.set_title("RGB Image")
    ax4.imshow(rgb_image)

    fig.canvas.manager.set_window_title('3. Negative Image Algorithm')
    plt.show()


# main (tirar daqui)
# filename = os.path.join('', 'red.png')
filename = os.path.join('', 'yiq-test.png')

original_image = io.imread(filename)

# print('Convertendo para o espaço de cores YIQ')
yiq_image = RGBtoYIQ(original_image)

rgb_image = YIQtoRGB(yiq_image)

# print('Gerando o negativo da imagem')
negative_image = negative(original_image)

print("Original Image\n", original_image[0][0], "\n")
print("YIQ Image\n", yiq_image[0][0], "\n")
print("RGB Image\n", rgb_image[0][0], "\n")
# print("Negative Image\n", negative_image[0][0], "\n")


if(np.array_equal(original_image, rgb_image)):
    print('sucess')
else:
    print('failure')


show_result_plot(original_image, negative_image,
                 yiq_image, rgb_image)
