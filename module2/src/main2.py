# 1.
# main1.py

from skimage import io
from os import path
import numpy as np
from math import sqrt, pow
import time
from utils.image_plot import get3dImageShape, showResultPlot
from utils.histogram_expansion import calculateHistogramExpansion
from discrete_cosine_transform import DCT1d, IDCT1d

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


I_approximation = []
# for row_index in range(0, Xk.shape[0]):
# Xk.shape[0]*Xk.shape[1]
# Resultado com somente 2 mil cossenos
for n in range(0, round((Xk.shape[0]*Xk.shape[1])/2)):
  # print('n:', n)
  # print("\033c", end="")
  # # Retorna o índice do valor máximo
  # max_values = np.amax(np.absolute(Xk))

  # # Retorna as coordenadas do índice de valor máximo
  # ij = np.unravel_index(max_values, Xk.shape)

  # coordinates = np.where(Xk == np.amax(Xk))
  coordinates = np.where(np.absolute(Xk) == np.amax(np.absolute(Xk)))

  i = coordinates[0][0]
  j = coordinates[1][0]

  I_approximation.append({
    "i": i,
    "j": j,
    "value": Xk[i][j]
  })

  # print('ij:', i, j)

  # print('Xk:', Xk[i][j])

  Xk[i][j] = 0

# print(I_approximation)

Xk = np.zeros([Xk.shape[0], Xk.shape[1]])

for index in range(0, len(I_approximation)):
  i = I_approximation[index]['i']
  j = I_approximation[index]['j']
  value = I_approximation[index]['value']

  Xk[i][j] = value

# print(Xk[0][0])
# print(Xk[0][1])
# print(Xk[2][5])
# print(Xk[0][3])
# print(Xk[0][4])
# print(Xk[1][1])
# exit()
# Xk[0][0] = dc_value

  # print('i,j', i, j)
  # print('=', Xk[i][j])

  # if (i == 0 and j == 0):
  #   print('Nível DC =', Xk[i][j])
  # else:
  #   Xk[i][j] = 0
  
  # print('(', x, y, ')')

  # I_approximation.append(Xk[x][y])

  # Xk[x][y] = 0

# print(I_approximation)
# exit()
# print('------')
# print(Xk)

# for i in range(0, Xk.shape[0]):
#   print(Xk[i])
# --------------------------- Transformada DCT Inversa (IDCT) de X[k] ---------------------------

# H - função de transferência do filtro
# d(k,l) - é a distância euclidiana do coeficiente (k,l) até a origem
# fc - é a distância de corte até a origem
# n >= 1 é a ordem do filtro
# def lowPassButterworthFilter(d, fc, n, cut_off_frequency):

#   for k in range(0, d.shape[0]):
#     for l in range(0, d.shape[1]):

#       H = 1/(sqrt(1 + pow((d[k, l]/fc), 2*n) ))

#       # As frequências acima de FC (frequência de corte) 
#       # são eliminadas e as abaixo de FC passam pelo filtro  
#       if (H >= cut_off_frequency):
#         print('H:', H, 'fc:', fc)
#         d[k][l] = 0

#   return d

# Xk = lowPassButterworthFilter(Xk, 10, 1, 0.5)

xn = np.empty([Xk.shape[0], Xk.shape[1]])

# Imagem transformada linha a linha pela IDCT 1D
for i in range(0, Xk.shape[0]):
  xn[i] = IDCT1d(Xk[i])

# Imagem transformada coluna a coluna pela IDCT 1D
for j in range(0, xn.shape[1]):
  xn[ :,j] = IDCT1d(xn[ :,j])

# print(xn)

# Realiza o recorte entre [0, 255]
# Xk = np.clip(Xk, 0, 255)

# # Aplicando expansão de histograma
# # getImageHistogramExpansion
# # expansão de histograma para [0, 255]
# for i in range(Xk.shape[0]):
#   for j in range(Xk.shape[1]):
#     Xk[i][j] = T(Xk[i][j], Xk)

# Zerando nível DC
Xk[0][0] = 0

I = get3dImageShape(I)
Xk = get3dImageShape(Xk)
xn = get3dImageShape(xn)

end = time.time()
print('FULL DCT Execution Time:', round(end - start), 's')

showResultPlot({
  'Imagem de Entrada': I,
  'Imagem com DCT (Ida)': Xk,
  'Imagem com DCT (Volta)': xn
})
