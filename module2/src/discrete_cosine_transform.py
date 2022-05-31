# Transformada Cosseno Discreta
# discrete_cosine_transform.py

import numpy as np
from math import sqrt, cos, pi

def DCT1d(x):
  """ 
  Calcula a DCT (Transformada Cosseno Discreta) de 1 dimensão, 
  onde dado o x[n] (sinal) obtemos a parcela da amplitude X[k].

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

    # if (k == 0):
    #   print('k=', k, 'n=', n, X[k])

  return X

def IDCT1d(X):
  """ 
  Calcula a IDCT (Transformada DCT inversa) de 1 dimensão, 
  onde dado o X[k] (importância dos cossenos, dado pela Amplitude
   de cada cosseno) obtemos o sinal x[n].

  Parameters
  ----------
  X : list
    X[k] representa a parcela da amplitude do cosseno.

  Returns
  -------
  x[n] : list
    é o sinal resultante da soma de todos os N cossenos 
    da família.
  """

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


def compressImage(Xk, nCoefficients):

  I_approximation = []

  for n in range(0, nCoefficients):
    # print('n:', n)
    # print("\033c", end="")

    # coordinates = np.where(Xk == np.amax(Xk))
    coordinates = np.where(np.absolute(Xk) == np.amax(np.absolute(Xk)))

    i = coordinates[0][0]
    j = coordinates[1][0]

    I_approximation.append({
      "i": i,
      "j": j,
      "value": Xk[i][j]
    })

    # Zerando para encontrar o próximo maior coeficiente
    Xk[i][j] = 0

  # Recriando o array X[K] comprimido 
  Xk = np.zeros([Xk.shape[0], Xk.shape[1]])

  for index in range(0, len(I_approximation)):
    i = I_approximation[index]['i']
    j = I_approximation[index]['j']
    value = I_approximation[index]['value']

    Xk[i][j] = value

  return Xk

