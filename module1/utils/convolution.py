# Convolução
# convolution.py

import numpy as np

# example = np.array([
#     [6, 15, 12],
#     [12, 6, 12],
#     [12, 3, 6]
# ])

# https://colab.research.google.com/github/xn2333/OpenCV/blob/master/Image_Processing_in_Python_Final.ipynb#scrollTo=TFTzLBgyOJPY
# https://en.wikipedia.org/wiki/Frobenius_inner_product
# example = np.array([
#     [12, 6, 0],
#     [15, 12, 0],
#     [6, 12, 0]
# ])

# example = np.array([
#     [8, 16, 11],
#     [11, 8, 11],
#     [11, 1, 8]
# ])

example = np.array([
    [11, 8, 0],
    [16, 11, 0],
    [8, 11, 0]
])

mask = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

print("Example:\n", example, "\n")

# Rebatendo a máscara
print("Mask:\n", mask, "\n")

# 1. Invertendo a ordem das colunas da máscara
flipped_column_arr = np.fliplr(mask)
# 2. Invertendo a ordem das linhas da máscara
flipped_row_arr = np.flipud(flipped_column_arr)


print("Máscara rebatida pela coluna:\n", flipped_column_arr, "\n")

print("Máscara rebatida pela linha:\n", flipped_row_arr, "\n")


# r = np.inner(
#     example,  flipped_row_arr)


# print("r:\n", r, "\n")


# print("total:\n", np.sum(r))

# Number of rows
# print(example.shape)

correlation_sum = 0
convolution_sum = 0
for i in range(example.shape[0]):
    # print("example:\n", example[i], "\n")
    # print("mask:\n", flipped_row_arr[i], "\n")

    # print("r:\n", np.inner(example[i], flipped_row_arr[i]), "\n")

    correlation_sum += np.inner(example[i], mask[i])

    convolution_sum += np.inner(example[i], flipped_row_arr[i])

print("sem rebatimento: correlação")
print(correlation_sum)

print("com rebatimento: convolução")
print(convolution_sum)
