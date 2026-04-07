import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return x ** 2

def f2(x):
    return 1 + x ** 3

def f3(x):
    return np.sqrt(np.clip(1 - x ** 2, 0, None))

def monte_carlo(func, a, b, H, n):
    x = np.random.uniform(a, b, n)
    y = np.random.uniform(0, H, n)

    abaixo = y <= func(x)

    estimativa = (b - a) * H * np.sum(abaixo) / n

    return estimativa, x[abaixo], y[abaixo], x[~abaixo], y[~abaixo]

def plotar(func, a, b, H, n, titulo):
    est, xd, yd, xf, yf = monte_carlo(func, a, b, H, n)

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.scatter(xf, yf, s=3, color="red",  alpha=0.5, label="Acima da curva")
    ax.scatter(xd, yd, s=3, color="blue", alpha=0.5, label="Abaixo da curva")

    x_curva = np.linspace(a, b, 500)
    ax.plot(x_curva, func(x_curva), color="black", lw=2)

    ax.set_xlim(a, b)
    ax.set_ylim(0, H)
    ax.set_title(f"{titulo}  |  n={n:,}  |  Estimativa = {est:.5f}")
    ax.legend(loc="upper left", markerscale=3)
    plt.tight_layout()
    plt.show()


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("  Valor inválido, tente novamente.")

def ler_int_positivo(mensagem):
    while True:
        try:
            v = int(input(mensagem))
            if v > 0:
                return v
        except ValueError:
            pass
        print("  Valor inválido, tente novamente.")


if __name__ == "__main__":
    N_LISTA = [50, 500, 5000, 50000]
    print("\n=== Integral 1: ∫ x² dx  [a=0, b=3, H=9] ===")
    a1, b1, H1 = 0, 3, 9.0
    n1 = ler_int_positivo("Número de pontos: ")

    for n in N_LISTA:
        est, *_ = monte_carlo(f1, a1, b1, H1, n)
        print(f"  n={n:>6,}  →  estimativa = {est:.5f}")

    print(f"\nGerando gráficos para n = {n1}...")
    plotar(f1, a1, b1, H1, n1, "∫ x² dx")

    # ── Integral 2: parâmetros via input ──────
    print("\n=== Integral 2: ∫ (1 + x³) dx ===")
    a2 = ler_float("  a = ")
    b2 = ler_float("  b = ")
    H2 = ler_float("  H (altura máxima da caixa) = ")
    n2 = ler_int_positivo("Número de pontos: ")

    for n in N_LISTA:
        est, *_ = monte_carlo(f2, a2, b2, H2, n)
        print(f"  n={n:>6,}  →  estimativa = {est:.5f}")

    print(f"\nGerando gráficos para n = {n2}...")
    plotar(f2, a2, b2, H2, n2, "∫ (1+x³) dx")

    # ── Integral 3: parâmetros via input ──────
    print("\n=== Integral 3: ∫ √(1 − x²) dx ===")
    a3 = ler_float("  a = ")
    b3 = ler_float("  b = ")
    H3 = ler_float("  H (altura máxima da caixa) = ")
    n3 = ler_int_positivo("Número de pontos: ")

    for n in N_LISTA:
        est, *_ = monte_carlo(f3, a3, b3, H3, n)
        print(f"  n={n:>6,}  →  estimativa = {est:.5f}")

    print(f"\nGerando gráficos para n = {n3}...")
    plotar(f3, a3, b3, H3, n3, "∫ √(1−x²) dx")
