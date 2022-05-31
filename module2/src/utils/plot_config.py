# Funções para ajudar na exibição dos plots das imagens
# plot_config.py

import numpy as np
from matplotlib import pyplot as plt
from colorama import Fore, Style
import tkinter
import matplotlib
import sys
from os import path
from skimage import io

matplotlib.use('TkAgg')

def showResultPlot(images_dict):

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
    #   print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Image TYPE - GRAY")
    #   print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Binary Image Format Convertion!")

      for i in range(image_3d.shape[0]):
          for j in range(image_3d.shape[1]):
              image_3d[i][j] = [I[i][j], I[i][j], I[i][j]]

      return image_3d.astype(np.uint8)
  else:
    #   print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Image TYPE - RGB")
      return I

def printResultStacktrace(color, msg, value):
    print(f"{color}{msg}:{Style.RESET_ALL} {value}")


def getImageInputInfo():
    # Image Argument
    image_name = str(sys.argv[1].split('=')[1])

    # Limpa terminal
    print("\033c", end="")

    filename = path.join('assets/images/', image_name)
    I = io.imread(filename)

    R = I.shape[0]
    C = I.shape[1]
    RxC = R*C
    printResultStacktrace(Fore.GREEN, "Imagem de entrada", image_name)
    printResultStacktrace(Fore.GREEN, "R (Número de linhas)", R)
    printResultStacktrace(Fore.GREEN, "C (Número de colunas)", C)
    printResultStacktrace(Fore.GREEN, "Tamanho da imagem RxC", RxC)

    return {"Image": I, "RxC": RxC}


# Remova banda Alpha das imagens
# I = I[:,:,:3]

# Transformando para imagem em tons cinza
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