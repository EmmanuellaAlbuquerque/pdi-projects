# Transformada Cosseno Discreta
# discrete_cosine_transform.py

from skimage import io
from os import path
import numpy as np
from math import sqrt, cos, pi
from matplotlib import pyplot as plt
from colorama import Fore, Style

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
    X[k] = round(constant * ck * summation, 2)

  return X


# x[k] - IDCT

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

print(I.shape)

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

# Calcula a DCT 2D de I (imagem de entrada) através da Separabilidade
Xk = np.empty([I.shape[0], I.shape[1]])

# Imagem transformada linha a linha pela DCT 1D
for i in range(0, I.shape[0]):
  Xk[i] = DCT1d(I[i])

# Imagem transformada coluna a coluna pela DCT 1D
for j in range(0, Xk.shape[1]):
  Xk[ :,j] = DCT1d(Xk[ :,j])


print('Nível DC:', Xk[0][0])
# Zerando nível DC
Xk[0][0] = 0

# Realiza o recorte entre [0, 255]
Xk = np.clip(Xk, 0, 255)

# Aplicando expansão de histograma
# getImageHistogramExpansion
# expansão de histograma para [0, 255]
for i in range(Xk.shape[0]):
  for j in range(Xk.shape[1]):
    Xk[i][j] = T(Xk[i][j], Xk)

I = get3dImageShape(I)
Xk = get3dImageShape(Xk)

show_result_plot({
  'Imagem de Entrada': I,
  'Imagem com Transformada Cosseno Discreta Aplicada': Xk
})


