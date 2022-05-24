# Testing Module of Digital Image Processing Functions
# results2_main.py

import os
from skimage import io
from dimgprocessing_module import RGBtoYIQ, YIQtoRGB, negative, show_result_plot

# ------------------------ Setup initial configuration ------------------------

# Carregando imagem de entrada
filename = os.path.join('images/', 'other-fruits-bowl.jpg')
# filename = os.path.join('images/', 'positive-color.png')

original_image = io.imread(filename, plugin='pil')

# ------------------------ 2. Negativo ------------------------

# 2.1 - Negativo RGB(banda a banda)

# Gerando o negativo da imagem
negative_image = negative(original_image)

# 2.2 - Negativo na banda Y, com posterior conversão para RGB

# Convertendo para o espaço de cores YIQ
yiq_image = RGBtoYIQ(original_image)

# Gerando o negativo na banda Y da imagem
yiq_negative_image = negative(yiq_image, mode='yiq')

# Convertendo de (Y)IQ Negativo para RGB
rgb_image = YIQtoRGB(yiq_negative_image)

show_result_plot({
    "Imagem Original": original_image,
    "Negativo em RGB": negative_image,
    "Negativo em Y": rgb_image,
})
