
# import testing.results1_main
# import testing.results2_main
import testing.results3_main

# # 3.

# # Carregando imagem de entrada
# filename = os.path.join('', 'black-line-center.png')
# # filename = os.path.join('', 'yiq-test.png')
# # filename = os.path.join('', 'correlation_test.png')
# # filename = os.path.join('', 'julian.jpg')
# # filename = os.path.join('', 'boat.png')
# # filename = os.path.join('', 'lenna-bw.png')
# # filename = os.path.join('', 'sobel.png')
# # filename = os.path.join('', 'einstein.png')
# # filename = os.path.join('', '20191126093552.jpg')
# # filename = os.path.join('', 'chimney.png')
# # filename = os.path.join('', 'apple.png')

# image = io.imread(filename, plugin='pil')
# # image = io.imread(filename, plugin='pil', as_gray=True)

# # Black and White Array Format
# # grayscale_array_image = color.rgb2gray(image)

# if (len(image.shape) != 3):
#     print('Binary image')
#     image = color.gray2rgb(image)

# # print(image)
# # exit()

# # -------------------- Definição da máscara usada --------------------

# # Filtro Box
# # box_mask = np.array([[1/9]*3]*3)
# # box_mask = np.array([[1/25]*5]*5)
# box_mask = np.array([[1/49]*7]*7)
# # box_mask = np.array([[1/225]*15]*15)
# # box_mask = np.array([[1/2401]*49]*49)

# sobel_mask_horizontal = np.array([
#     [-1, -2, -1],
#     [0, 0, 0],
#     [1, 2, 1]
# ])

# sobel_mask_vertical = np.array([
#     [-1, 0, 1],
#     [-2, 0, 2],
#     [-1, 0, 1]
# ])

# mask = sobel_mask_horizontal

# # -------------------------------------------------------


# # separado nas bandas rgb


# # pivot
# # def calculateCorrelation(image, mask, offset=0):

# # Testando a média RGB
# # correlation = Correlation(image, mask, filter_type='median')
# # g_array = correlation.calculate()

# # # Exibindo os resultados
# # show_result_plot({
# #     "Imagem Original": image,
# #     "Filtro Mediana nas bandas RGB": g_array
# # })


# # 4. Filtro mediana m x n, com m e n ímpares, sobre a banda Y do YIQ.

# # Convertendo para o espaço de cores YIQ
# # yiq_image = RGBtoYIQ(image)

# # print('====> image ', image[100][100])
# # print('====> yiq ', yiq_image[100][100])

# # # correlation = Correlation(image, mask, filter_type='median')
# # correlation = Correlation(yiq_image, mask, filter_type='yiq-median')
# # correlation = Correlation(image, mask)
# # g_array = correlation.calculate()

# # print('====> g ', g_array[100][100])

# # for i in range(yiq_image.shape[0]):
# #     for j in range(yiq_image.shape[1]):

# #         try:
# #             yiq_image[i][j][0] = g_array[i][j][0]
# #         except:
# #             continue

# # print('====> somente y deve estar modificado', yiq_image[100][100])
# # g_array = YIQtoRGB(yiq_image)

# # print('====> rgb', g_array[100][100])

# # Exibindo os resultados
# # show_result_plot({
# #     "Imagem Original": image,
# #     # "Box Filter Image": g_array.astype(np.uint8)
# #     # "Filtro Média (Box) 49x49": g_array.astype(np.uint8)
# #     "Filtro Mediana banda Y": g_array
# # })

# # show_result_plot({
# #     "Imagem Original": image,
# #     "Imagem Original": image
# # })

# # print(image[0][0])
# # print(image)
# # print(grayscale_array_image)
