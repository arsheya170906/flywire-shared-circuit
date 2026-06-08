import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

res = json.load(open("star_results.json"))
hub = res["FAFB"]["out"]["hub"]
N = 1872
SHOW = 72  # draw a sample of the 1871 leaves so the star stays readable

fig, ax = plt.subplots(figsize=(7.2, 7.2))
ang = np.linspace(0, 2 * np.pi, SHOW, endpoint=False)
lx, ly = np.cos(ang), np.sin(ang)
for x, y in zip(lx, ly):
    ax.add_patch(FancyArrowPatch((0, 0), (x * 0.9, y * 0.9), arrowstyle='-|>',
                 mutation_scale=8, color='#b0b7c3', lw=0.6, alpha=0.8, zorder=1))
ax.scatter(lx, ly, s=70, c='#4C9BE8', edgecolors='white', lw=0.8, zorder=2)
ax.scatter([0], [0], s=900, c='#E8554E', edgecolors='white', lw=1.5, zorder=3)
ax.text(0, 0, "hub", ha='center', va='center', color='white', fontsize=11, fontweight='bold', zorder=4)
ax.text(0, -1.32, f"Shared divergence motif  -  N = {N} neurons (1 hub, 1871 targets)\n"
        f"showing {SHOW} targets  -  isomorphic across FAFB, MCNS, MAOL",
        ha='center', va='center', fontsize=9.5)
ax.set_xlim(-1.45, 1.45)
ax.set_ylim(-1.5, 1.4)
ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.savefig("circuit_graph.png", dpi=200, bbox_inches='tight')
