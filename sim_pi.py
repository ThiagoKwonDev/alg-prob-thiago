import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

iterations_list = [100, 1000, 5000, 10000, 20000, 50000, 100000]

fig = plt.figure(figsize=(20, 24))
fig.patch.set_facecolor('#0f0f1a')
gs = gridspec.GridSpec(3, 3, figure=fig, hspace=0.4, wspace=0.3)

for idx, n in enumerate(iterations_list):
    x = np.random.uniform(0, 1, n)
    y = np.random.uniform(0, 1, n)

    d = np.sqrt((x - 0.5)**2 + (y - 0.5)**2)
    inside = d < 0.5
    j = np.sum(inside)
    pi_approx = 4 * (j / n)

    row, col = divmod(idx, 3)
    ax = fig.add_subplot(gs[row, col])
    ax.set_facecolor('#0f0f1a')

    ax.scatter(x[~inside], y[~inside], s=0.5 if n > 5000 else 2,
               color='#E24B4A', alpha=0.6, linewidths=0)
    ax.scatter(x[inside], y[inside], s=0.5 if n > 5000 else 2,
               color='#378ADD', alpha=0.6, linewidths=0)

    circle = plt.Circle((0.5, 0.5), 0.5, color='white', fill=False,
                         linewidth=0.8, alpha=0.5)
    ax.add_patch(circle)

    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-0.02, 1.02)
    ax.set_aspect('equal')
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_edgecolor('#333355')
        spine.set_linewidth(0.5)

    fmt = f"{n:,}".replace(",", ".")
    ax.set_title(f"{fmt} iterações\nπ ≈ {pi_approx:.6f}",
                 color='white', fontsize=10, fontweight='bold', pad=8)

ax_legend = fig.add_subplot(gs[2, 2])
ax_legend.set_facecolor('#0f0f1a')
ax_legend.axis('off')
ax_legend.scatter([], [], color='#378ADD', s=40, label='Dentro do círculo (d < 0.5)')
ax_legend.scatter([], [], color='#E24B4A', s=40, label='Fora do círculo (d ≥ 0.5)')
ax_legend.legend(loc='center', fontsize=10, frameon=False, labelcolor='white', markerscale=2)
ax_legend.set_title("Legenda", color='white', fontsize=11, fontweight='bold')

ax_legend.text(0.5, 0.15,
    "d = √((x−0.5)² + (y−0.5)²)\nπ = 4 × (j / N)",
    color='#aaaacc', fontsize=9, ha='center', va='center',
    transform=ax_legend.transAxes,
    fontfamily='monospace')

fig.suptitle('Simulação de Monte Carlo — Aproximação de π',
             color='white', fontsize=16, fontweight='bold', y=0.98)

plt.savefig('monte_carlo_pi.png', dpi=150, bbox_inches='tight', facecolor='#0f0f1a')
plt.show()