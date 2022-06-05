# 1.
# main1.py

from skimage import io
from os import path
import numpy as np
from math import sqrt, pow, log
import time
from utils.plot_config import get3dImageShape, showResultPlot, printResultStacktrace, getImageInputInfo
from utils.histogram_expansion import calculateHistogramExpansion
from discrete_cosine_transform import DCT1d, IDCT1d, compressImage
from colorama import Fore, Style
import copy

I_info = getImageInputInfo()
I = I_info["Image"]
RxC = I_info["RxC"]

# O parâmetro n é um inteiro no intervalo [0, RxC-1].
nCoefficients = int(input('Digite o número de coeficientes a serem preservados na imagem: '))

if (not (nCoefficients >= 0 and nCoefficients <= RxC - 1)):
  print("O número de coeficientes(n), deve estar entre o intervalo [0, RxC-1]")

start = time.time()

# --------------------------- Transformada DCT de x[n] ---------------------------
printResultStacktrace(Fore.YELLOW, "DCT", "")
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

Xk_compressed = compressImage(copy.deepcopy(Xk), nCoefficients)

# --------------------------- Transformada DCT Inversa (IDCT) de X[k] ---------------------------
printResultStacktrace(Fore.YELLOW, "IDCT", "")
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

# Zerando nível DC
Xk[0][0] = 0

# Imagem para visualização
# Ajuste fino para exibição pós DCT (módulo normalizado)
Xk = np.absolute(Xk)
Xk_expanded = np.empty([Xk.shape[0], Xk.shape[1]])

printResultStacktrace(Fore.YELLOW, "Expansão de histograma", "")
# Aplicando expansão de histograma
# expansão de histograma para [0, 255]
for i in range(0, Xk.shape[0]):
  for j in range(0, Xk.shape[1]):
    Xk_expanded[i][j] = calculateHistogramExpansion(Xk[i][j], Xk)

# Zerando nível DC
# Xk[0][0] = 0

I = get3dImageShape(I)
Xk = get3dImageShape(Xk)
Xk_expanded = get3dImageShape(Xk_expanded)
Xk_compressed = get3dImageShape(Xk_compressed)
xn = get3dImageShape(xn)
xn_compressed = get3dImageShape(xn_compressed)

end = time.time()
print('FULL DCT Execution Time:', round(end - start), 's')

showResultPlot({
  'Imagem de Entrada': I,
  'DCT (sem nível DC)': Xk_expanded,
  f'Aproximação de I com {nCoefficients+1} coeficientes': Xk_compressed,
  'IDCT (Volta)': xn,
  f'IDCT com {nCoefficients+1} coeficientes': xn_compressed
})
