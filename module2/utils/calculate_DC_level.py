import numpy as np
from math import sqrt, cos, pi
from os import path
from skimage import io

# Entradas
filename = path.join('../src/assets/images/', 'lena256.png')
I = io.imread(filename)
print(I.shape)

ck = sqrt(1/2)
cl = sqrt(1/2)
constant = (2/(sqrt(I.shape[0] * I.shape[1]))) * ck * cl

total_sum = I[0][0] * cos(((2 * 0 + 1) * 0 * pi) 
                        / (2 * I.shape[0])) * cos(((2 * 0 + 1) * 0 * pi) 
                        / (2 * I.shape[1])) 

X = constant * total_sum

print(X)