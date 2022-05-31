# 1.
# main1.py

from skimage import io
from os import path
import numpy as np
from math import sqrt, pow
import time
from utils.image_plot import get3dImageShape, showResultPlot
from utils.histogram_expansion import calculateHistogramExpansion
from discrete_cosine_transform import DCT1d, IDCT1d, compressImage
from colorama import Fore, Style
import copy

filename = path.join('assets/images/', 'lena256.png')
I = io.imread(filename)

start = time.time()

# --------------------------- Transformada DCT de x[n] ---------------------------

# Calcula a DCT 2D de I (imagem de entrada) através da Separabilidade
Xk = np.empty([I.shape[0], I.shape[1]])

# Imagem transformada linha a linha pela DCT 1D
for i in range(0, I.shape[0]):
  Xk[i] = DCT1d(I[i])

# Imagem transformada coluna a coluna pela DCT 1D
for j in range(0, Xk.shape[1]):
  Xk[ :,j] = DCT1d(Xk[ :,j])

# Exibindo nível DC
print(f"{Fore.GREEN}Nível DC:{Style.RESET_ALL} {round(Xk[0][0], 2)}")

# Resultado com somente 2 mil cossenos (metade)
# nCoefficients = round((Xk.shape[0]*Xk.shape[1])/2)
nCoefficients = round((Xk.shape[0]*Xk.shape[1])/2 - 20000)
Xk_compressed = compressImage(copy.deepcopy(Xk), nCoefficients)

# --------------------------- Transformada DCT Inversa (IDCT) de X[k] ---------------------------

xn = np.empty([Xk.shape[0], Xk.shape[1]])
xn_compressed = np.empty([Xk.shape[0], Xk.shape[1]])

# Imagem transformada linha a linha pela IDCT 1D
for i in range(0, Xk.shape[0]):
  xn[i] = IDCT1d(Xk[i])
  xn_compressed[i] = IDCT1d(Xk_compressed[i])

# Imagem transformada coluna a coluna pela IDCT 1D
for j in range(0, xn.shape[1]):
  xn[ :,j] = IDCT1d(xn[ :,j])
  xn_compressed[ :,j] = IDCT1d(xn_compressed[ :,j])

# Realiza o recorte entre [0, 255]
# Xk = np.clip(Xk, 0, 255)

# Aplicando expansão de histograma
# expansão de histograma para [0, 255]
for i in range(Xk.shape[0]):
  for j in range(Xk.shape[1]):
    Xk[i][j] = calculateHistogramExpansion(Xk[i][j], Xk)

# Zerando nível DC
Xk[0][0] = 0

I = get3dImageShape(I)
Xk = get3dImageShape(Xk)
Xk_compressed = get3dImageShape(Xk_compressed)
xn = get3dImageShape(xn)
xn_compressed = get3dImageShape(xn_compressed)

end = time.time()
print('FULL DCT Execution Time:', round(end - start), 's')

showResultPlot({
  'Imagem de Entrada': I,
  'DCT (sem nível DC)': Xk,
  f'Aproximação de I com {nCoefficients} coeficientes': Xk_compressed,
  'IDCT (Volta)': xn,
  f'IDCT com {nCoefficients} coeficientes': xn_compressed
})
