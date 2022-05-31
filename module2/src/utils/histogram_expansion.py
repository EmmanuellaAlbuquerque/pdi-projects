# Calculando expansão de histograma
# histogram_expansion.py

import numpy as np
from colorama import Fore, Style

# S = T(r) ; r = valor de entrada
def calculateHistogramExpansion(r, image, L=256):
    """ 
    Calcula a expansão de histograma.

    Parameters
    ----------
    r : number

    Returns
    -------
    X[k] : int
        valor expandido entre 0 e L(default=256).
    """

    rmin = np.min(image)
    rmax = np.max(image)

    # Caso ocorra divisão por zero
    if (rmax == rmin):
        print(
            f"{Fore.YELLOW}ALERT:{Style.RESET_ALL} Não foi possível realizar a expansão! rmax = rmin")
        exit()
    return round(((r - rmin)/(rmax - rmin)) * (L - 1))

