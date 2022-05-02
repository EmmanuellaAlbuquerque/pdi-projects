
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import match_template

# Imagem de entrada
woman = io.imread('images/Woman.png', as_gray=True)

# Template (sub-image)
woman_eye_template = io.imread('images/Woman_eye.png', as_gray=True)


def findMatch():

    # Retorna uma matriz com os valores entre [-1, 1] correspondentes ao
    # coeficiente de correlação
    result = match_template(woman, woman_eye_template)

    # Retorna o índice do valor máximo
    max_values = np.argmax(result)

    # Retorna as coordenadas do índice de valor máximo
    ij = np.unravel_index(max_values, result.shape)

    # Retorna a última coordenada
    x, y = ij[::-1]

    return (x, y)


# ------------------------- MAIN -------------------------

# Configurando o plot
ax1 = plt.subplot(1, 4, 1)
ax2 = plt.subplot(1, 4, 2)
ax3 = plt.subplot(1, 4, 3)
ax4 = plt.subplot(1, 4, 4, sharex=ax3, sharey=ax3)

# Definindo o plot do template
ax1.imshow(woman_eye_template, cmap=plt.cm.gray)
ax1.set_axis_off()
ax1.set_title('Template (sub-image)')

# Definindo o plot da imagem de entrada
ax2.imshow(woman, cmap=plt.cm.gray)
ax2.set_axis_off()
ax2.set_title('Imagem de entrada')

# Encontrando a primeira maior correlação
(x1, y1) = findMatch()

# Destacando a região de maior correlação
h_template, w_template = woman_eye_template.shape
rect = plt.Rectangle((x1, y1), w_template, h_template,
                     edgecolor='r', facecolor='none')
ax2.add_patch(rect)

# Adicionando um quadrado branco na
# primeira correlação do olho
for i in range(y1-1, y1+h_template+1):  # i,y - linha - inicio altura
    for j in range(x1-1, x1+w_template+1):  # j, x - coluna - inicio largura
        woman[i][j] = 1

# Definindo o plot da imagem de entrada
# com o olho da primeira correlação removido
ax3.imshow(woman, cmap=plt.cm.gray)
ax3.set_axis_off()
ax3.set_title('Imagem com o olho removido')

# Encontrando a segunda maior correlação
(x2, y2) = findMatch()

# Definindo o plot da segunda maior correlação
ax4.imshow(woman, cmap=plt.cm.gray)
ax4.set_axis_off()
ax4.set_title('Imagem de saída')

# Destacando a segunda região de maior correlação
h_template, w_template = woman_eye_template.shape
rect = plt.Rectangle((x2, y2), w_template, h_template,
                     edgecolor='r', facecolor='none')
ax4.add_patch(rect)

plt.show()
