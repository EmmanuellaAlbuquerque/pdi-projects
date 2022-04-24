
import numpy as np
import os
from skimage import io, color
from dimgprocessing_module import show_result_plot


class Correlation:
    def __init__(self, image, mask, offset=0, filter_type='mask'):
        self.image = image
        self.mask = mask
        self.offset = offset
        self.filter = filter_type

        self.num_rows_mask = mask.shape[0]
        self.num_columns_mask = mask.shape[1]

        self.num_rows_image = image.shape[0]
        self.num_columns_image = image.shape[1]

        # Calculando a posição do pixel central da máscara
        self.central_mask_pixel_i = int((self.num_rows_mask - 1)/2)
        self.central_mask_pixel_j = int((self.num_columns_mask - 1)/2)

        self.final_i = self.num_rows_image - self.central_mask_pixel_i
        self.final_j = self.num_columns_image - self.central_mask_pixel_j

        self.g = []

    def setNeighborhood(self, actual_i, actual_j):
        R_neighborhood = []
        G_neighborhood = []
        B_neighborhood = []

        # Definindo vizinhança de acordo com a tamanho da máscara
        for row in range(-self.central_mask_pixel_i, self.central_mask_pixel_i+1, 1):
            for column in range(-self.central_mask_pixel_j, self.central_mask_pixel_j+1, 1):

                pixel_rgb = self.image[actual_i+row][actual_j+column]
                [R, G, B] = pixel_rgb

                R_neighborhood.append(R)
                G_neighborhood.append(G)
                B_neighborhood.append(B)

        return [R_neighborhood, G_neighborhood, B_neighborhood]

    def calculate(self):
        # A máscara desliza sobre a imagem de entrada
        # Pixel a pixel da imagem de entrada
        for i in range(self.central_mask_pixel_i, self.final_i):
            for j in range(self.central_mask_pixel_j, self.final_j):

                try:

                    [
                        R_neighborhood,
                        G_neighborhood,
                        B_neighborhood
                    ] = self.setNeighborhood(i, j)

                    self.applyFilter(
                        R_neighborhood,
                        G_neighborhood,
                        B_neighborhood)

                except IndexError:
                    # print('> sem extensão por zero.')
                    continue

                except BaseException as err:
                    print(f"Unexpected {err=}, {type(err)=}")
                    raise

        return self.gToArray()

    def applyFilter(self, R_neighborhood, G_neighborhood, B_neighborhood):
        if (self.filter == 'median'):
            self.g.append(
                [round(np.median(R_neighborhood)),
                 round(np.median(G_neighborhood)),
                 round(np.median(B_neighborhood))
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
            for q in range(R_v.shape[0]):
                for w in range(R_v.shape[1]):

                    R_v[q][w] = R_neighborhood[k]
                    G_v[q][w] = G_neighborhood[k]
                    B_v[q][w] = B_neighborhood[k]
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

            self.g.append([round(R_correlation_sum), round(
                G_correlation_sum), round(B_correlation_sum)])

    def gToArray(self):
        try:
            g_array = np.empty([self.num_rows_image - 2 * self.central_mask_pixel_i,
                                self.num_columns_image - 2 * self.central_mask_pixel_j,
                                3])
        except ValueError:
            print('Máscara maior que a imagem! image =',
                  self.image.shape, 'mask =', self.mask.shape)
            exit()

        print(self.image.shape)
        print(g_array.shape)

        k = 0
        for i in range(g_array.shape[0]):
            for j in range(g_array.shape[1]):
                g_array[i][j] = self.g[k]
                k += 1

        return g_array
