# 1.
# main2.py

import numpy as np
import time
from utils.plot_config import get3dImageShape, showResultPlot, getAudioInputInfo
from discrete_cosine_transform import DCT1d, IDCT1d, lowPassButterworthFilterAudio
import pyaudio

# sinal s, em formato .wav
audio_info = getAudioInputInfo()
audio = audio_info["audio"]
audio_size = audio_info["size"]

p = pyaudio.PyAudio()
BITRATE = 44100 # number of frames per second/frameset.
stream = p.open(format = p.get_format_from_width(1), 
            channels = 1, 
            rate = BITRATE, 
            output = True)
stream.write(audio)
stream.stop_stream()
stream.close()
p.terminate()

exit()

audio = audio[:100]
audio_size = 100

start = time.time()

# --------------------------- Transformada DCT de x[n] ---------------------------

# Calcula a DCT 1D do audio de entrada
Xk = DCT1d(audio)

# --------------------------- Aplicando filtro Butterworth ---------------------------

# aplicando o filtro Butterworth passa-baixas no domínio da frequência.
# H - função de transferência do filtro
# d(k,l) - é a distância euclidiana do coeficiente (k,l) até a origem
# fc - é a distância de corte até a origem
# n >= 1 é a ordem do filtro

fc = float(input('Digite (fc) a distância de corte até a origem: '))
n = int(input('Digite (n) a ordem do filtro, [n >= 1]: '))

# f(frequência em Hz), fc, n
f = np.empty([audio_size])

# fa que é frequência da amostragem, é o valor encontrado após aplicação da dct no audio?
# ou fa = 1/Ta

for k in range(0, audio_size):
    f1 = (Xk[k] / (2 * (audio_size - 1)))
    f[k] = k * f1

Xk = lowPassButterworthFilterAudio(f, fc, n)

audio = np.array([audio])
Xk = np.array([Xk])

audio = get3dImageShape(audio)
Xk = get3dImageShape(Xk)

end = time.time()
print('FULL DCT Execution Time:', round(end - start), 's')

showResultPlot({
  'Imagem de Entrada': audio,
  f'Imagem com filtro Butterworth passa-baixas n={n}': Xk
})
