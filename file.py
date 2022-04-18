from skimage import io, data
from matplotlib import pyplot as plt
import os


def negative(image_path):
    """Filtro para interver a cor, isto é, gerar o
       negativo das imagens.

    Args:
        image_path (str): o caminho da imagem.

    Returns:
        ndarray : o array com as bandas invertidas.
    """
    print('Generating Negative Image')

    original_image = io.imread(image_path)

    L = pow(2, 8)  # 256
    negative_image = (L - 1) - original_image

    return (original_image, negative_image)


def show_result_plot(original_image, negative_image):
    #  PLOT CONFIG: 1 row X 2 column
    n_row, n_col = 1, 2
    fig, (ax1, ax2) = plt.subplots(n_row, n_col, constrained_layout=True)

    ax1.set_title('Original Image')
    ax1.imshow(original_image)

    ax2.set_title("Negative Image")
    ax2.imshow(negative_image)

    fig.canvas.manager.set_window_title('3. Negative Image Algorithm')
    plt.show()


# main (tirar daqui)
# filename = os.path.join('', 'red.png')
filename = os.path.join('', 'red.png')

(original_image, negative_image) = negative(filename)

print("Original Image\n", original_image, "\n")
print("Negative Image\n", negative_image, "\n")

# show_result_plot(original_image, negative_image)
