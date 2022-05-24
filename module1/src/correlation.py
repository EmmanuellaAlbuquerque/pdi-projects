# Correlation Class Module of Digital Image Processing
# correlation.py

import numpy as np
from colorama import Fore, Style


class Correlation:
    def __init__(self, image, mask, offset=0, filter_type='mask'):
        self.image = image
        self.mask = mask
        self.offset = offset
        self.filter = filter_type
        print(f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} {self.filter.capitalize()} Filter")

        self.g = []

        self.R_neighborhood = []
        self.G_neighborhood = []
        self.B_neighborhood = []

        self.num_rows_mask = mask.shape[0]
        self.num_columns_mask = mask.shape[1]

        self.num_rows_image = image.shape[0]
        self.num_columns_image = image.shape[1]

        # Calculando a posição do pixel central da máscara
        self.central_mask_pixel_i = int((self.num_rows_mask - 1)/2)
        self.central_mask_pixel_j = int((self.num_columns_mask - 1)/2)

    def setNeighborhood(self, actual_i, actual_j):
        self.R_neighborhood = []
        self.G_neighborhood = []
        self.B_neighborhood = []

        # Definindo vizinhança de acordo com a tamanho da máscara
        for row_index in range(-self.central_mask_pixel_i, self.central_mask_pixel_i+1, 1):
            for column_index in range(-self.central_mask_pixel_j, self.central_mask_pixel_j+1, 1):

                try:

                    pixel_i = actual_i + row_index
                    pixel_j = actual_j + column_index

                    # Tratando casos de acesso no array com valores negativos
                    if (pixel_i < 0 or pixel_j < 0):
                        raise IndexError

                    pixel_rgb = self.image[pixel_i][pixel_j]

                    [R, G, B] = pixel_rgb

                    self.R_neighborhood.append(R)
                    self.G_neighborhood.append(G)
                    self.B_neighborhood.append(B)

                except IndexError:
                    # Adiciona a extensão por zero
                    self.R_neighborhood.append(0)
                    self.G_neighborhood.append(0)
                    self.B_neighborhood.append(0)
                    continue

    def calculate(self):
        # A máscara desliza sobre a imagem de entrada
        # Pixel a pixel da imagem de entrada
        # Mechanism to slide the mask
        for i in range(0, self.num_rows_image):
            for j in range(0, self.num_columns_image):

                try:

                    self.setNeighborhood(i, j)

                    self.applyFilter()

                except BaseException as err:
                    print(f"Unexpected {err=}, {type(err)=}")
                    raise

        return self.gToArray()

    def applyFilter(self):
        # Filtro Mediana
        if (self.filter == 'median'):
            self.g.append(
                [round(np.median(self.R_neighborhood)),
                 round(np.median(self.G_neighborhood)),
                 round(np.median(self.B_neighborhood))
                 ])
        else:

            # Vizinhança v(i,j) => R(i,j), G(i,j), B(i,j)
            R_v = np.empty(
                [self.num_rows_mask, self.num_columns_mask])
            G_v = np.empty(
                [self.num_rows_mask, self.num_columns_mask])
            B_v = np.empty(
                [self.num_rows_mask, self.num_columns_mask])

            # Transformando a lista de vizinhaça em um array
            k = 0
            for i in range(R_v.shape[0]):
                for j in range(R_v.shape[1]):

                    R_v[i][j] = self.R_neighborhood[k]
                    G_v[i][j] = self.G_neighborhood[k]
                    B_v[i][j] = self.B_neighborhood[k]
                    k += 1

            # Realizando o cálculo de correlação
            R_correlation_sum = 0
            G_correlation_sum = 0
            B_correlation_sum = 0
            for v_index in range(R_v.shape[0]):

                R_correlation_sum += np.inner(
                    R_v[v_index], self.mask[v_index])
                G_correlation_sum += np.inner(
                    G_v[v_index], self.mask[v_index])
                B_correlation_sum += np.inner(
                    B_v[v_index], self.mask[v_index])

            if (self.filter == 'sobel'):

                if (R_correlation_sum < 0):
                    R_correlation_sum = abs(R_correlation_sum)
                    G_correlation_sum = abs(G_correlation_sum)
                    B_correlation_sum = abs(B_correlation_sum)

                # Borda mais evidente
                if (R_correlation_sum > 255):
                    R_correlation_sum = 255
                    G_correlation_sum = 255
                    B_correlation_sum = 255
                # Se não for 0, não possui uma edge (borda) e continua 0 (preto)

            self.g.append([round(R_correlation_sum), round(
                G_correlation_sum), round(B_correlation_sum)])

    def gToArray(self):
        try:
            g_array = np.empty([self.num_rows_image,
                                self.num_columns_image,
                                3])
        except ValueError:
            print('Máscara maior que a imagem! image =',
                  self.image.shape, 'mask =', self.mask.shape)
            exit()

        k = 0
        for i in range(g_array.shape[0]):
            for j in range(g_array.shape[1]):
                g_array[i][j] = self.g[k]
                k += 1

        if (self.offset != 0):
            g_array = g_array + self.offset
            g_array = np.clip(g_array, 0, 255)

        return g_array.astype(np.uint8)
