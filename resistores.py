import numpy as np
import matplotlib.pyplot as plt

def simular_e_plotar(n=1000):
    R1_nom, R2_nom, R3_nom = 100, 200, 300
    V_nom = 14.8
    
    R1 = np.random.uniform(R1_nom * 0.95, R1_nom * 1.05, n)
    R2 = np.random.uniform(R2_nom * 0.95, R2_nom * 1.05, n)
    R3 = np.random.uniform(R3_nom * 0.95, R3_nom * 1.05, n)
    V_fonte = np.random.uniform(V_nom * 0.93, V_nom * 1.07, n)

    Req_paralelo = (R2 * R3) / (R2 + R3)
    Req_total = R1 + Req_paralelo
    I_total = V_fonte / Req_total
    V1 = I_total * R1
    V_paralelo = V_fonte - V1
    
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    
    axs[0].hist(Req_total, bins=30, color='skyblue', edgecolor='black')
    axs[0].set_title('Distribuição de Req (Ω)')
    axs[0].set_xlabel('Resistência (Ω)')
    axs[0].set_ylabel('Frequência')

    axs[1].hist(I_total, bins=30, color='salmon', edgecolor='black')
    axs[1].set_title('Distribuição de Corrente Total (A)')
    axs[1].set_xlabel('Corrente (A)')
    axs[1].set_ylabel('Frequência')

    axs[2].hist(V_fonte, bins=30, alpha=0.5, label='V Fonte', color='gray')
    axs[2].hist(V_paralelo, bins=30, alpha=0.7, label='V no Paralelo (R2/R3)', color='green')
    axs[2].set_title('Distribuição de Tensões (V)')
    axs[2].set_xlabel('Tensão (V)')
    axs[2].set_ylabel('Frequência')
    axs[2].legend()

    plt.tight_layout()
    plt.show()

simular_e_plotar(1000)
