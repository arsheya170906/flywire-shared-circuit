import json
import numpy as np
import matplotlib.pyplot as plt

res = json.load(open("star_results.json"))
datasets = ["MCNS", "FAFB", "MAOL", "BANC", "MANC"]
kinds = [("out", "Out-star (divergence)"), ("in", "In-star (convergence)"),
         ("recip", "Reciprocal rosette")]
colors = ["#2C6FB0", "#6FB02C", "#B0742C"]

x = np.arange(len(datasets))
w = 0.26
fig, ax = plt.subplots(figsize=(8, 4.2))
for i, (k, lbl) in enumerate(kinds):
    ax.bar(x + (i - 1) * w, [res[d][k]["size"] for d in datasets], w, label=lbl, color=colors[i])

ax.axhline(1872, ls="--", lw=1, color="#444")
ax.text(4.3, 1912, "submitted N = 1872", ha="right", fontsize=9, color="#444")
ax.set_xticks(x)
ax.set_xticklabels([f"{d}\n(no optic lobe)" if d == "MANC" else d for d in datasets])
ax.set_ylabel("Largest connected motif (nodes)")
ax.set_title("Shared-circuit size per dataset, by motif family")
ax.legend(frameon=False, fontsize=9)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()
plt.savefig("../figures/motif_sizes.png", dpi=200)
