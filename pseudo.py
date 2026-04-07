import matplotlib.pyplot as plt
import numpy as np

def gerar_serie_glc(n_max, a=3, b=5, m=31, f0=2):
    x = np.arange(n_max + 1)
    f = np.zeros(n_max + 1)
    f[0] = f0
    for n in range(1, n_max + 1):
        f[n] = (a * f[n-1] + b) % m
    return x, f

def criar_dashboard(lista_n, titulo_principal):
    fig, axes = plt.subplots(3, 2, figsize=(14, 10))
    fig.suptitle(titulo_principal, fontsize=18, fontweight='bold', color='#1A5276')
    
    axes = axes.flatten()

    for i, n in enumerate(lista_n):
        x, y = gerar_serie_glc(n)
        
        largura_linha = 1.0 if n <= 100 else 0.4
        
        axes[i].plot(x, y, color='#2980B9', linewidth=largura_linha)
        axes[i].set_title(f"n = {n}", fontsize=12, fontweight='bold')
        axes[i].set_ylim(0, 32)
        axes[i].grid(True, linestyle='--', alpha=0.4)
        
        axes[i].spines['top'].set_visible(False)
        axes[i].spines['right'].set_visible(False)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

iteracoes_curto = [10, 20, 30, 40, 50, 60]
criar_dashboard(iteracoes_curto, "Análise GLC: Curto Prazo (10 a 60 iterações)")

iteracoes_longo = [70, 80, 90, 100, 1000, 10000]
criar_dashboard(iteracoes_longo, "Análise GLC: Longo Prazo e Densidade (70 a 10.000 iterações)")

plt.show()