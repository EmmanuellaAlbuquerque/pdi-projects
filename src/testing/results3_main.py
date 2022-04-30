# Testing Module of Digital Image Processing Functions
# results3_main.py

import os
from skimage import io
from correlation import Correlation
from dimgprocessing_module import show_result_plot
import numpy as np
import matplotlib.pyplot as plt
from colorama import Fore, Style

TYPE = 'GRAY'

# 3. Correlação m x n sobre R, G e B.


# Calculando expansão de histograma
# S = T(r) ; r = valor de entrada
def T(r, image, L=256):
    rmin = np.min(image)
    rmax = np.max(image)

    # Caso ocorra divisão por zero
    if (rmax == rmin):
        print(
            f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Não foi possível realizar a expansão! rmax = rmin")
        exit()
    return round(((r - rmin)/(rmax - rmin)) * (L - 1))


# Carregando imagem de entrada
# filename = os.path.join('images/', 'black-line-center.png')
# filename = os.path.join('images/', 'lenna-bw.png')
# filename = os.path.join('images/', 'lenna.png')
# filename = os.path.join('images/', 'einstein.png')
# filename = os.path.join('images/', 'Woman.png')
filename = os.path.join('images/', 'boat.png')

image = io.imread(filename, plugin='pil')

image_3d = np.empty([image.shape[0], image.shape[1], 3])
if (len(image.shape) != 3):
    print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Image TYPE - GRAY")
    print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Binary Image Format Convertion!")

    for i in range(image_3d.shape[0]):
        for j in range(image_3d.shape[1]):
            image_3d[i][j] = [image[i][j], image[i][j], image[i][j]]
    image = image_3d
else:
    print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Image TYPE - RGB")
    TYPE = 'RGB'
    image_3d = image

# -------------------- Definição da máscara usada --------------------

# Filtro Box
box_mask_3x3 = np.array([[1/9]*3]*3)
box_mask_5x5 = np.array([[1/25]*5]*5)
box_mask_7x7 = np.array([[1/49]*7]*7)
box_mask_15x15 = np.array([[1/225]*15]*15)
box_mask_49x49 = np.array([[1/2401]*49]*49)

# Máscara Sobel Horizontal
sobel_mask_horizontal = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

# Máscara Sobel Vertical
sobel_mask_vertical = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

# Máscara Atual
mask = sobel_mask_horizontal

print('Image Shape:', image.shape)
grayscale_image = []
grayscale_image_3d = image_3d

# Color image to black and white converter
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        [R, G, B] = image[i][j]

        # Converte para GRAY
        if (TYPE == 'RGB'):
            gray_result = round((int(R) + int(G) + int(B))/3)

            grayscale_image_3d[i][j] = [
                gray_result, gray_result, gray_result]

        grayscale_image.append(R)

grayscale_image_3d_expansion = np.empty([image.shape[0], image.shape[1], 3])
grayscale_image_expansion = []

for i in range(grayscale_image_3d.shape[0]):
    for j in range(grayscale_image_3d.shape[1]):

        # Passando somente o valor de R, pois R=B=G
        S = T(grayscale_image_3d[i][j][0], grayscale_image_3d)

        grayscale_image_expansion.append(S)
        grayscale_image_3d_expansion[i][j] = [S, S, S]

# Correlação COM EXPANSÃO
correlation_grayscale = Correlation(
    grayscale_image_3d, mask, filter_type='sobel')
g_array_grayscale = correlation_grayscale.calculate()

# Correlação SEM EXPANSÃO
correlation_expansion = Correlation(
    grayscale_image_3d_expansion, mask, filter_type='sobel')
g_array_expansion = correlation_expansion.calculate()

show_result_plot({
    "Imagem Original (Grayscale)": grayscale_image_3d.astype(np.uint8),
    "Resultado Correlação Sem Expansão": g_array_grayscale.astype(np.uint8),
    "Imagem Com Expansão": grayscale_image_3d_expansion.astype(np.uint8),
    "Resultado Correlação Com Expansão": g_array_expansion.astype(np.uint8),
})

# Definindo Plot do Histograma
plt.style.use('seaborn-deep')
plt.title('Histograma da Imagem')
plt.xlabel('Nível de cinza')
plt.ylabel('Frequência')

plt.hist([grayscale_image, grayscale_image_expansion],
         256, rwidth=0.9, label=['Original', 'Com a expansão'])

plt.legend(loc='upper right')
plt.show()

# "Box Filter Image": g_array.astype(np.uint8)
# "Filtro Média (Box) 49x49": g_array.astype(np.uint8)
