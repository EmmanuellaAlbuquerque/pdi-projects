# 1.
# main2.py

import numpy as np
import time
from math import sqrt, dist
from utils.plot_config import get3dImageShape, showResultPlot, getImageInputInfo, printResultStacktrace
from discrete_cosine_transform import DCT1d, IDCT1d, lowPassButterworthFilter
from colorama import Fore, Style

I_info = getImageInputInfo()
I = I_info["Image"]
R = I_info["R"]
C = I_info["C"]

start = time.time()

# Obtendo dados para aplicação do filtro Butterworth
fc = float(input('Digite (fc) a distância de corte até a origem: '))
n = int(input('Digite (n) a ordem do filtro, [n >= 1]: '))

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

# --------------------------- Aplicando filtro Butterworth ---------------------------
printResultStacktrace(Fore.YELLOW, "Aplicação Filtro Butterworth", "")

# aplicando o filtro Butterworth passa-baixas no domínio da frequência.
# H - função de transferência do filtro
# d(k,l) - é a distância euclidiana do coeficiente (k,l) até a origem
# fc - é a distância de corte até a origem
# n >= 1 é a ordem do filtro

# distância euclidiana do coeficiente (k,l) até a origem
D = np.zeros([I.shape[0], I.shape[1]])
for u in range(0, R):
  for v in range(0, C):
    D[u][v] = sqrt(pow(u, 2) + pow(v, 2))

# d(Imagem no domínio da frequência), fc, n, cut_off_frequency
Xk = lowPassButterworthFilter(D, fc, n, Xk)

# --------------------------- Transformada DCT Inversa (IDCT) de X[k] ---------------------------
printResultStacktrace(Fore.YELLOW, "IDCT", "")

xn = np.empty([Xk.shape[0], Xk.shape[1]])

# Imagem transformada linha a linha pela IDCT 1D
for i in range(0, Xk.shape[0]):
  xn[i] = IDCT1d(Xk[i])

# Imagem transformada coluna a coluna pela IDCT 1D
for j in range(0, xn.shape[1]):
  xn[ :,j] = IDCT1d(xn[ :,j])

end = time.time()
print('FULL DCT Execution Time:', round(end - start), 's')

showResultPlot({
  'Imagem de Entrada': get3dImageShape(I),
  f'Imagem com filtro Butterworth passa-baixas n={n}': get3dImageShape(Xk),
  'Imagem de Saída': get3dImageShape(xn)
})
