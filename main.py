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
#     # "Banda Y do YIQ": yiq_image,
#     "Original Image": original_image,
#     "(Y)IQ Negative Image RGB": rgb_image,
# })
