# 1.
# main2.py

import numpy as np
import time
from utils.plot_config import get3dImageShape, showResultPlot, getImageInputInfo
from discrete_cosine_transform import DCT1d, IDCT1d, lowPassButterworthFilter

I_info = getImageInputInfo()
I = I_info["Image"]

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

# --------------------------- Aplicando filtro Butterworth ---------------------------

# aplicando o filtro Butterworth passa-baixas no domínio da frequência.
# H - função de transferência do filtro
# d(k,l) - é a distância euclidiana do coeficiente (k,l) até a origem
# fc - é a distância de corte até a origem
# n >= 1 é a ordem do filtro

fc = float(input('Digite (fc) a distância de corte até a origem: '))
n = int(input('Digite (n) a ordem do filtro, [n >= 1]: '))

# d(Imagem no domínio da frequência), fc, n, cut_off_frequency
Xk = lowPassButterworthFilter(Xk, fc, n)

# --------------------------- Transformada DCT Inversa (IDCT) de X[k] ---------------------------

xn = np.empty([Xk.shape[0], Xk.shape[1]])

# Imagem transformada linha a linha pela IDCT 1D
for i in range(0, Xk.shape[0]):
  xn[i] = IDCT1d(Xk[i])

# Imagem transformada coluna a coluna pela IDCT 1D
for j in range(0, xn.shape[1]):
  xn[ :,j] = IDCT1d(xn[ :,j])

I = get3dImageShape(I)
Xk = get3dImageShape(Xk)
xn = get3dImageShape(xn)

end = time.time()
print('FULL DCT Execution Time:', round(end - start), 's')

showResultPlot({
  'Imagem de Entrada': I,
  f'Imagem com filtro Butterworth passa-baixas n={n}': Xk,
  'Imagem com DCT (Volta)': xn
})
