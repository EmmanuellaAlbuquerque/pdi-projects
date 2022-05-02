# Testing Module of Digital Image Processing Functions
# results1_main.py

from colorama import Fore, Style
import numpy as np
from dimgprocessing_module import RGBtoYIQ, YIQtoRGB, show_result_plot
from skimage import io
import os

# ------------------------ Setup initial configuration ------------------------

# Carregando imagem de entrada
# filename = os.path.join('images/', 'testpat.1k.color.tif')
# filename = os.path.join('images/', 'mountains-house.png')
filename = os.path.join('images/', 'flower.jpeg')
original_image = io.imread(filename, plugin='pil')

# ------------------------ 1. Conversão RGB-YIQ-RGB ------------------------

# Convertendo para o espaço de cores YIQ
yiq_image = RGBtoYIQ(original_image)

y_image = RGBtoYIQ(original_image, mode='y')

# Convertendo de YIQ para RGB
rgb_image = YIQtoRGB(yiq_image)

# Verificando conversão
if(np.array_equal(original_image, rgb_image)):
    print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Sucess RGB-YIQ-RGB (RGBtoYIQ, YIQtoRGB)")
else:
    print(f"{Fore.RED}ALERT:{Style.RESET_ALL} Failure RGB-YIQ-RGB (RGBtoYIQ, YIQtoRGB)")

# Exibindo os resultados
show_result_plot({
    "Imagem Original": original_image,
    "Imagem YIQ (somente para propósitos de teste)": yiq_image,
    "Imagem banda Y": y_image,
    "Imagem RGB": rgb_image
})
