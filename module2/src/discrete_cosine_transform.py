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

  for n in range(0, nCoefficients+1):
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

# H - função de transferência do filtro
# d(k,l) - é a distância euclidiana do coeficiente (k,l) até a origem
# fc - é a distância de corte até a origem
# n >= 1 é a ordem do filtro
def lowPassButterworthFilter(d, fc, n, Xk):

  for k in range(0, d.shape[0]):
    for l in range(0, d.shape[1]):

      H = 1/(sqrt(1 + pow((d[k, l]/fc), 2*n) ))

      # Passa Alta
      # H = 1/(sqrt(1 + pow((fc/(d[k, l])), 2*n) ))
      # print(H)
      
      Xk[k][l] = H * Xk[k][l]

      # passa altas
      # if (H <= 1/2):
      # if (H >= 1/2):
        # d[k][l] = 0
        # Xk[k][l] = 0
    
  return Xk

def lowPassButterworthFilterAudio(f, fc, n):

  for k in range(0, f.shape[0]):

      H = 1/(sqrt(1 + pow((f[k]/fc), 2*n) ))  
      
      # passa altas
      # if (H <= 1/2):
      if (H >= 1/2):
        f[k] = 0

  return f

def lowPassButterworthFilterAudio2(f, fc, n, Xk):

  for k in range(0, f.shape[0]):

      H = 1/(sqrt(1 + pow((f[k]/fc), 2*n) ))  

      Xk[k] = H * Xk[k]      
      # passa altas
      # if (H <= 1/2):
      # if (H >= 1/2):
      #   f[k] = 0

  return Xk
