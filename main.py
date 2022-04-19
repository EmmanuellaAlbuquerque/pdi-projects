# Testing Module of Digital Image Processing Functions
# main.py

import os
from skimage import io, data, color
from dimgprocessing_module import RGBtoYIQ, YIQtoRGB, negative, show_result_plot
import numpy as np
from colorama import Fore, Style

# ------------------------ Setup initial configuration ------------------------

# Carregando imagem de entrada
filename = os.path.join('', 'yiq-test.png')
original_image = io.imread(filename)

# ------------------------ 1. Conversão RGB-YIQ-RGB ------------------------

# Convertendo para o espaço de cores YIQ
yiq_image = RGBtoYIQ(original_image)

# Convertendo de YIQ para RGB
rgb_image = YIQtoRGB(yiq_image)

# Verificando conversão
if(np.array_equal(original_image, rgb_image)):
    print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Sucess RGB-YIQ-RGB (RGBtoYIQ, YIQtoRGB)")
else:
    print(f"{Fore.RED}ALERT:{Style.RESET_ALL} Failure RGB-YIQ-RGB (RGBtoYIQ, YIQtoRGB)")

# Exibindo os resultados
show_result_plot({
    "Original Image": original_image,
    "YIQ Image": yiq_image,
    "RGB Image": rgb_image
})

# ------------------------ 2 ------------------------

# print('Gerando o negativo da imagem')
negative_image = negative(original_image)

# print("Original Image\n", original_image[0][0], "\n")
# print("YIQ Image\n", yiq_image[0][0], "\n")
# print("RGB Image\n", rgb_image[0][0], "\n")
# print("Negative Image\n", negative_image[0][0], "\n")

# # Images
# images_dict = {
#     "Original Image": original_image,
#     "Negative Image": negative_image,
#     "YIQ Image": yiq_image,
#     "RGB Image": rgb_image
# }

# show_result_plot(images_dict)
