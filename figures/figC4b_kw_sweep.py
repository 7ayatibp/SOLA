"""Report Figure C4b: perfect-foresight wholesale NPV by battery energy and power (kW sweep, cycle-life wear basis).
Usage: python figC4b.py kw_sweep.csv out.png"""
import sys
import pandas as pd, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
d = pd.read_csv(sys.argv[1]); w = d[d.tariff == "wholesale"]
mods, kws = [1, 2, 3], [3, 5, 8, 10]
npv = np.array([[w[(w.modules == m) & (w.kW == k)].npv.iloc[0] for k in kws] for m in mods]) / 1000
net = np.array([[w[(w.modules == m) & (w.kW == k)].net_of_wear.iloc[0] for k in kws] for m in mods])
plt.rcParams.update({"font.family": ["Lato", "DejaVu Sans"], "font.size": 7.5, "text.color": "#231F20"})
fig, ax = plt.subplots(figsize=(16 / 2.54, 5.6 / 2.54), dpi=300)
cmap = LinearSegmentedColormap.from_list("o", ["#F4F2EE", "#F2B27A", "#E8731A"])
ax.imshow(npv, cmap=cmap, aspect="auto", vmin=npv.min(), vmax=npv.max())
for i, m in enumerate(mods):
    for j, k in enumerate(kws):
        feasible = k <= 4 * m
        if not feasible:
            ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, facecolor="white", edgecolor="#CFCAC4", lw=0.6, zorder=2))
            ax.text(j, i, f"above the {4 * m} kW module limit", ha="center", va="center", fontsize=6.2, color="#8C8782", zorder=3)
            continue
        ax.text(j, i - 0.12, f"NPV −${-npv[i, j]:.1f}k", ha="center", va="center", fontsize=7, weight="bold",
                color="#231F20" if feasible else "#8C8782")
        ax.text(j, i + 0.22, f"${net[i, j]:,.0f}/yr net of wear", ha="center", va="center", fontsize=6.2,
                color="#231F20" if feasible else "#8C8782")
        if not feasible:
            ax.add_patch(plt.Rectangle((j - 0.5, i - 0.5), 1, 1, facecolor="white", edgecolor="#CFCAC4", lw=0.6, zorder=2))
            ax.text(j, i, f"above {4 * m} kW module limit", ha="center", va="center", fontsize=6.2, color="#8C8782", zorder=3)
            continue
        if (m, k) == (2, 5):
            ax.add_patch(plt.Rectangle((j - 0.48, i - 0.48), 0.96, 0.96, fill=False, edgecolor="#231F20", lw=1.4))
ax.set_xticks(range(len(kws))); ax.set_xticklabels([f"{k} kW" for k in kws])
ax.set_yticks(range(len(mods))); ax.set_yticklabels([f"{m} module{'s' if m > 1 else ''} ({7.8 * m:.1f} kWh)" for m in mods])
ax.set_xlabel("Charge and discharge power (battery and controller)")
for s in ax.spines.values(): s.set_visible(False)
ax.tick_params(length=0)
fig.tight_layout(); fig.savefig(sys.argv[2], dpi=300, facecolor="white"); print("saved")
