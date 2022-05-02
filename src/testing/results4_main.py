# Testing Module of Digital Image Processing Functions
# results4_main.py

import os
import numpy as np
from dimgprocessing_module import show_result_plot, RGBtoYIQ, YIQtoRGB
from skimage import io
from correlation import Correlation

# 4. Filtro mediana m x n, com m e n ímpares, sobre a banda Y do YIQ.

# Carregando imagem de entrada

# Ruído Salt-and-Pepper
# filename = os.path.join('images/', 'salt-and-pepper.png')
# filename = os.path.join('images/', 'Woman.png')
# filename = os.path.join('images/', 'defective-pixels.png')
filename = os.path.join('images/', 'apple.png')
# filename = os.path.join('images/', 'color-factory-illuminated-wall.jpg')

image = io.imread(filename, plugin='pil')

# Remove (A) from RGBA images
# image = image[..., :3]
# print(image)

# Filtro Box
box_mask_3x3 = np.array([[1/9]*3]*3)
box_mask_5x5 = np.array([[1/25]*5]*5)
box_mask_7x7 = np.array([[1/49]*7]*7)
box_mask_15x15 = np.array([[1/225]*15]*15)
box_mask_49x49 = np.array([[1/2401]*49]*49)

mask = box_mask_15x15

# 4.1 Testando a Mediana RGB
correlation = Correlation(image, mask, filter_type='median')
rgb_g_array = correlation.calculate()

# 4.2 Testando a Mediana na banda Y

# Convertendo para o espaço de cores YIQ
yiq_image = RGBtoYIQ(image)

correlation = Correlation(yiq_image, mask, filter_type='median')
yqi_g_array = correlation.calculate()

# Alterando somente o valor da banda Y, após a correlação
for i in range(yiq_image.shape[0]):
    for j in range(yiq_image.shape[1]):

        try:
            yiq_image[i][j][0] = yqi_g_array[i][j][0]
        except:
            continue

yqi_g_array = YIQtoRGB(yiq_image)

# Exibindo os resultados
show_result_plot({
    "Imagem Original": image,
    "Filtro Mediana nas bandas RGB": rgb_g_array,
    "Filtro Mediana na banda Y": yqi_g_array
})
