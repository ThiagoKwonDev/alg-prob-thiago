import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np

def sptinik(m, s):
    p0, q0 = 0.322232431088, 0.099348462606
    p1, q1 = 1.0, 0.588581570495
    p2, q2 = 0.342242088547, 0.531103462366
    p3, q3 = 0.204231210245e-1, 0.103537752850
    p4, q4 = 0.453642210148e-4, 0.385607006340e-2

    u = random.random()

    if u < 0.5:
        t = math.sqrt(-2.0 * math.log(u))
    else:
        t = math.sqrt(-2.0 * math.log(1.0 - u))

    p = p0 + t * (p1 + t * (p2 + t * (p3 + t * p4)))
    q = q0 + t * (q1 + t * (q2 + t * (q3 + t * q4)))

    if u < 0.5:
        z = (p / q) - t
    else:
        z = t - (p / q)

    return m + s * z

if __name__ == "__main__":
    carteirinha = 40073818
    desvioPadrao = 3818
    random.seed(time.time())
    
    valores = [sptinik(carteirinha, desvioPadrao) for _ in range(10000)]

    plt.figure()
    plt.hist(valores, bins=50, density=True)
    plt.title("Histograma - Distribuição Normal (SPUTNIK)")
    plt.xlabel("Valores")
    plt.ylabel("Densidade")
    plt.show()
    
    freq, bins = np.histogram(valores, bins=20)

    plt.figure()
    plt.bar(bins[:-1], freq, width=(bins[1] - bins[0]))
    plt.title("Distribuição de Frequência")
    plt.xlabel("Intervalos de Classe")
    plt.ylabel("Frequência")
    plt.show()