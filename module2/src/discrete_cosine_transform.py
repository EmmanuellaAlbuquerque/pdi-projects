# Transformada Cosseno Discreta
# discrete_cosine_transform.py

from skimage import io
from os import path
import numpy as np
from math import sqrt, cos, pi
from matplotlib import pyplot as plt
from colorama import Fore, Style
import time

# X[k] - DCT
def DCT1d(x):
  """ 
  Calcula a DCT de 1 dimensão, onde dado o  x[n] obtemos 
  a parcela da amplitude X[k].

  Parameters
  ----------
  x : list
    x[n] é o sinal resultante da soma de todos os N cossenos 
    da família.

  Returns
  -------
  X[k] : list
    representa a parcela da amplitude do cosseno.
  """

  N = x.shape[0]
  X = np.array([0.0]*N)

  constant = sqrt(2/N)

  for k in range(0, N):
    summation = 0
    for n in range(0, N):

      summation += x[n] * cos((2 * pi * k * n)/(2 * N) + (k * pi)/(2 * N))
    
    # ck test
    ck = sqrt(1/2) if k == 0 else 1
    X[k] = constant * ck * summation

  return X


# x[k] - IDCT
def IDCT1d(X):

  N = X.shape[0]
  x = np.array([0.0]*N)

  constant = sqrt(2/N)

  for n in range(0, N):
    summation = 0
    for k in range(0, N):
      # ck test
      ck = sqrt(1/2) if k == 0 else 1

      # x[n] 
      summation += ck * X[k] * cos((2 * pi * k * n)/(2 * N) + (k * pi)/(2 * N))

    x[n] = constant * summation
  
  return x

def show_result_plot(images_dict):

    number_of_images = len(images_dict)
    n_row, n_col = 1, number_of_images

    # PLOT CONFIG
    fig, axs = plt.subplots(
        n_row, n_col, constrained_layout=True)

    if (type(axs) != np.ndarray):
        print(
            f'{Fore.RED}ALERT:{Style.RESET_ALL}'
            ' Exiba pelo menos 2 images (a original e a de saída)'
            ' para visualizar os resultados.')
        exit()

    images_names_list = list(images_dict.keys())

    for i in range(number_of_images):
        image_name = images_names_list[i]
        matrix = images_dict[image_name]

        axs[i].set_title(image_name)
        axs[i].imshow(matrix)

    fig.canvas.manager.set_window_title('Results')
    plt.show()

def get3dImageShape(I):
  # Convertendo gray shape [x] para [x,x,x] shape
  image_3d = np.empty([I.shape[0], I.shape[1], 3])

  if (len(I.shape) != 3):
      print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Image TYPE - GRAY")
      print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Binary Image Format Convertion!")

      for i in range(image_3d.shape[0]):
          for j in range(image_3d.shape[1]):
              image_3d[i][j] = [I[i][j], I[i][j], I[i][j]]

      return image_3d.astype(np.uint8)
  else:
      print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Image TYPE - RGB")
      return I

# Calculando expansão de histograma
# S = T(r) ; r = valor de entrada
def T(r, image, L=256):
    rmin = np.min(image)
    rmax = np.max(image)

    # Caso ocorra divisão por zero
    if (rmax == rmin):
        print(
            f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Não foi possível realizar a expansão! rmax = rmin")
        exit()
    return round(((r - rmin)/(rmax - rmin)) * (L - 1))


filename = path.join('assets/images/', 'lena256.png')
# filename = path.join('assets/images/', 'cosseno-vertical.png')
I = io.imread(filename)

# I = np.array([[11.53, 5.93, 2.15, 0.47, -0.54, 0.96, 3.69, 4.11],
#              [-11.53, -5.93, -2.15, -0.47, 0.54, -0.96, -3.69, -4.11]])

# print(I.shape, 'entry:', I)

# Remova banda Alpha das imagens
# I = I[:,:,:3]

# I_gray = np.empty([I.shape[0], I.shape[1]])

# for i in range(I.shape[0]):
#     for j in range(I.shape[1]):
#         [R, G, B] = I[i][j]

#         # Converte para GRAY Scale:
#         gray_result = round((int(R) + int(G) + int(B))/3)

#         I_gray[i][j] = gray_result

# I = I_gray
# print(I_gray.shape)
# print(I_gray)
# exit()

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

# print(Xk.round(2))

print(Xk)
print(Xk.shape)

# dc_value = Xk[0][0]
# Zerando nível DC
# Xk[0][0] = 0

I_approximation = []
# for row_index in range(0, Xk.shape[0]):
# Xk.shape[0]*Xk.shape[1]
# Resultado com somente 2 mil cossenos
for n in range(0, round((Xk.shape[0]*Xk.shape[1])/2) - 30000):
  print('n:', n)
  print("\033c", end="")
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

I = get3dImageShape(I)
Xk = get3dImageShape(Xk)
xn = get3dImageShape(xn)

end = time.time()
print('FULL DCT Execution Time:', round(end - start), 's')

show_result_plot({
  'Imagem de Entrada': I,
  'Imagem com DCT (Ida)': Xk,
  'Imagem com DCT (Volta)': xn
})
