# 1.
# best_ACs_coefficients.py

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
  exit()

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

# --------------------------- Configurando DCT para visualização ---------------------------
# Zerando nível DC
Xk[0][0] = 0

# Ajuste fino para exibição pós DCT (módulo normalizado)
Xk = np.absolute(Xk)

# log(|DCT|+1) normalizado
Xk_log = np.empty([Xk.shape[0], Xk.shape[1]])
Xk_compressed_log = np.empty([Xk.shape[0], Xk.shape[1]])
for i in range(0, Xk.shape[0]):
  for j in range(0, Xk.shape[1]):
    Xk_log[i][j] = log(abs(Xk[i][j]) + 1)
    Xk_compressed_log[i][j] = log(abs(Xk_compressed[i][j]) + 1)

# DCT de visualização sem nível DC
Xk_expanded = np.empty([Xk.shape[0], Xk.shape[1]])

# DCT de visualização log(|DCT|+1)
Xk_log_expanded = np.empty([Xk.shape[0], Xk.shape[1]])
Xk_compressed_log_expanded = np.empty([Xk.shape[0], Xk.shape[1]])

printResultStacktrace(Fore.YELLOW, "Expansão de histograma", "")

# Aplicando expansão de histograma para [0, 255]
for i in range(0, Xk.shape[0]):
  for j in range(0, Xk.shape[1]):
    Xk_expanded[i][j] = calculateHistogramExpansion(Xk[i][j], Xk)

    Xk_log_expanded[i][j] = calculateHistogramExpansion(Xk_log[i][j], Xk_log)
    Xk_compressed_log_expanded[i][j] = calculateHistogramExpansion(Xk_compressed_log[i][j], Xk_compressed_log)

end = time.time()
print('FULL DCT Execution Time:', round(end - start), 's')

showResultPlot({
  'Imagem de Entrada': get3dImageShape(I),
  'DCT (sem nível DC)': get3dImageShape(Xk_expanded),
  'log(|DCT|+1) normalizado': get3dImageShape(Xk_log_expanded),
  f'log(|DCT|+1) com {nCoefficients+1} coeficientes': get3dImageShape(Xk_compressed_log_expanded),
  # '(Volta)': get3dImageShape(xn),
  f'Imagem de Saída': get3dImageShape(xn_compressed)
})
