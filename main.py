# Testing Module of Digital Image Processing Functions
# main.py

import os
from skimage import io, data, color
from correlation import Correlation
from dimgprocessing_module import RGBtoYIQ, YIQtoRGB, negative, show_result_plot
import numpy as np
from colorama import Fore, Style
import matplotlib.pyplot as plt

# ------------------------ Setup initial configuration ------------------------

# Carregando imagem de entrada
filename = os.path.join('', 'yiq-test.png')
# original_image = io.imread(filename)
# filename = os.path.join('', 'testpat.1k.color.tif')
original_image = io.imread(filename, plugin='pil', as_gray=True)

# ------------------------ 1. Conversão RGB-YIQ-RGB ------------------------

# # Convertendo para o espaço de cores YIQ
# yiq_image = RGBtoYIQ(original_image)

# # Convertendo de YIQ para RGB
# rgb_image = YIQtoRGB(yiq_image)

# # Verificando conversão
# if(np.array_equal(original_image, rgb_image)):
#     print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Sucess RGB-YIQ-RGB (RGBtoYIQ, YIQtoRGB)")
# else:
#     print(f"{Fore.RED}ALERT:{Style.RESET_ALL} Failure RGB-YIQ-RGB (RGBtoYIQ, YIQtoRGB)")

# # Exibindo os resultados
# show_result_plot({
#     "Original Image": original_image,
#     "YIQ Image": yiq_image,
#     "RGB Image": rgb_image
# })

# ------------------------ 2. Negativo ------------------------

# 2.1 - Negativo RGB (banda a banda)

# # Gerando o negativo da imagem
# negative_image = negative(original_image)

# show_result_plot({
#     "Original Image": original_image,
#     "Negative Image": negative_image,
# })

# 2.2 - Negativo na banda Y, com posterior conversão para RGB

# # Convertendo para o espaço de cores YIQ
# yiq_image = RGBtoYIQ(original_image)

# # Gerando o negativo na banda Y da imagem
# yiq_negative_image = negative(yiq_image, mode='yiq')

# # Convertendo de (Y)IQ Negativo para RGB
# rgb_image = YIQtoRGB(yiq_negative_image)

# show_result_plot({
#     "Imagem Original": original_image,
#     "Negativo em Y": rgb_image,
# })

# 3.

# Carregando imagem de entrada
# filename = os.path.join('', 'black-line-center.png')
# filename = os.path.join('', 'yiq-test.png')
# filename = os.path.join('', 'correlation_test.png')
# filename = os.path.join('', 'julian.jpg')
# filename = os.path.join('', 'boat.png')
# filename = os.path.join('', 'lenna-bw.png')
# filename = os.path.join('', 'sobel.png')
filename = os.path.join('', 'einstein.png')
# filename = os.path.join('', '20191126093552.jpg')
# filename = os.path.join('', 'chimney.png')
# filename = os.path.join('', 'apple.png')

image = io.imread(filename, plugin='pil')
# image = io.imread(filename, plugin='pil', as_gray=True)

# Black and White Array Format
# grayscale_array_image = color.rgb2gray(image)

# if (len(image.shape) != 3):
#     print('Binary image')
#     image = color.gray2rgb(image)

# print(image)
# exit()

# -------------------- Definição da máscara usada --------------------

# Filtro Box
# box_mask = np.array([[1/9]*3]*3)
# box_mask = np.array([[1/25]*5]*5)
# box_mask = np.array([[1/49]*7]*7)
# box_mask = np.array([[1/225]*15]*15)
box_mask = np.array([[1/2401]*49]*49)

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

mask = sobel_mask_horizontal

# -------------------------------------------------------


# separado nas bandas rgb


# pivot
# def calculateCorrelation(image, mask, offset=0):


# 4. Filtro mediana m x n, com m e n ímpares, sobre a banda Y do YIQ.

# Convertendo para o espaço de cores YIQ
# yiq_image = RGBtoYIQ(image)

# print('====> image ', image[100][100])
# print('====> yiq ', yiq_image[100][100])

# # correlation = Correlation(image, mask, filter_type='median')
# correlation = Correlation(yiq_image, mask, filter_type='yiq-median')
# correlation = Correlation(image, mask)
# g_array = correlation.calculate()

# print('====> g ', g_array[100][100])

# for i in range(yiq_image.shape[0]):
#     for j in range(yiq_image.shape[1]):

#         try:
#             yiq_image[i][j][0] = g_array[i][j][0]
#         except:
#             continue

# print('====> somente y deve estar modificado', yiq_image[100][100])
# g_array = YIQtoRGB(yiq_image)

# print('====> rgb', g_array[100][100])

# Exibindo os resultados
# show_result_plot({
#     "Imagem Original": image,
#     # "Box Filter Image": g_array.astype(np.uint8)
#     # "Filtro Média (Box) 49x49": g_array.astype(np.uint8)
#     "Filtro Mediana banda Y": g_array
# })

# show_result_plot({
#     "Imagem Original": image,
#     "Imagem Original": image
# })

# print(image[0][0])
# print(image)
# print(grayscale_array_image)


grayscale_image = []
grayscale_image_3d = np.empty([image.shape[0], image.shape[1], 3])

# Color image to black and white converter
for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        [R, G, B] = image[i][j]

        # gray_result = round((int(R) + int(G) + int(B))/3)
        # grayscale_image.append(gray_result)
        # grayscale_image_3d[i][j] = [
        #     gray_result, gray_result, gray_result]

        grayscale_image.append(R)
        grayscale_image_3d[i][j] = [R, G, B]


# Calculando expansão de histograma
def T(r, image, L=256):
    rmin = np.min(image)
    rmax = np.max(image)

    # Caso ocorra divisão por zero
    if (rmax == rmin):
        print("Não foi possível realizar a expansão! rmax = rmin")
        exit()
    return round(((r - rmin)/(rmax - rmin)) * (L - 1))


# r = valor de entrada
# S = T(r)
# S = T(5, image)
# print(S)

grayscale_image_3d_expansion = np.empty([image.shape[0], image.shape[1], 3])
grayscale_image_expansion = []

print(np.min(grayscale_image_3d), np.max(grayscale_image_3d))
for i in range(grayscale_image_3d.shape[0]):
    for j in range(grayscale_image_3d.shape[1]):

        # Passando somente o valor de R, pois R=B=G
        S = T(grayscale_image_3d[i][j][0], grayscale_image_3d)

        grayscale_image_expansion.append(S)
        grayscale_image_3d_expansion[i][j] = [S, S, S]

print(np.min(grayscale_image_expansion), np.max(grayscale_image_expansion))


correlation_grayscale = Correlation(grayscale_image_3d, mask)
g_array_grayscale = correlation_grayscale.calculate()

correlation_expansion = Correlation(grayscale_image_3d_expansion, mask)
g_array_expansion = correlation_expansion.calculate()

show_result_plot({
    # "Imagem Original": image,
    "Imagem Original(Grayscale)": grayscale_image_3d.astype(np.uint8),
    "Resultado Correlação Sem Expansão": g_array_grayscale.astype(np.uint8),
    "Imagem Original(Expanded)": grayscale_image_3d_expansion.astype(np.uint8),
    "Resultado Correlação Com Expansão": g_array_expansion.astype(np.uint8),
})

plt.style.use('seaborn-deep')
plt.title('Histograma da Imagem')
plt.xlabel('Nível de cinza')
plt.ylabel('Frequência')
# plt.hist(idades, 5, rwidth=0.9, color='black')
plt.hist([grayscale_image, grayscale_image_expansion],
         256, rwidth=0.9, label=['Original', 'Com a expansão'])
plt.legend(loc='upper right')
plt.show()
