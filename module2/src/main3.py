# 1.
# main2.py

import numpy as np
import time
from utils.plot_config import get3dImageShape, showResultPlot, getAudioInputInfo, setAudioOutputInfo, printResultStacktrace
from discrete_cosine_transform import DCT1d, IDCT1d, lowPassButterworthFilterAudio
from colorama import Fore, Style
from datetime import datetime

# sinal s, em formato .wav
audio_info = getAudioInputInfo()
audio = audio_info["audio"]
audio_size = audio_info["size"]

hour = datetime.now().time().hour
minute = datetime.now().time().minute
print("Start at >", str(hour) +  ':' + str(minute))

# (fa = samplerate) frequência da amostragem
fa = audio_info["fa"]

start = time.time()

# Obtendo dados para aplicação do filtro Butterworth
fc = float(input('Digite (fc) a distância de corte até a origem: '))
n = int(input('Digite (n) a ordem do filtro, [n >= 1]: '))

# --------------------------- Transformada DCT de x[n] ---------------------------
printResultStacktrace(Fore.YELLOW, "DCT", "")
# Calcula a DCT 1D do audio de entrada
Xk = DCT1d(audio)

# --------------------------- Aplicando filtro Butterworth ---------------------------
printResultStacktrace(Fore.YELLOW, "Aplicação Filtro Butterworth", "")
# f(frequência em Hz), fc, n
f = np.empty([audio_size])

# f1, frequência fundamental a partir da qual todas as demais se formam 
f1 = (fa / (2 * (audio_size - 1)))

# Calculando as frequências em Hz
for k in range(0, audio_size):
    f[k] = k * f1

# aplicando o filtro Butterworth passa-baixas no domínio da frequência.
Xk = lowPassButterworthFilterAudio(f, fc, n, Xk)

# --------------------------- Transformada IDCT de X[k] ---------------------------
printResultStacktrace(Fore.YELLOW, "IDCT", "")

# Calcula a IDCT 1D
output = IDCT1d(Xk)
setAudioOutputInfo(output, 'output', fc, n)

end = time.time()
print('FULL DCT Execution Time:', round(end - start), 's')
