"""Report Figure C8: build-up of the wholesale pass-through import price by network period, 2023 averages (c/kWh).
Numbers come from wholesale_retail_price (Task 3.3) applied to 2023 NSW1 spot prices."""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SPOT = {"Off-peak\n(23:00-07:00)": 9.11, "Shoulder\n(07:00-19:00)": 9.23, "Peak\n(19:00-23:00)": 11.66, "All hours": 9.59}
NET = {"Off-peak\n(23:00-07:00)": 4.98, "Shoulder\n(07:00-19:00)": 12.39, "Peak\n(19:00-23:00)": 16.89, "All hours": 10.67}
TOU = {"Off-peak\n(23:00-07:00)": 15, "Shoulder\n(07:00-19:00)": 25, "Peak\n(19:00-23:00)": 40}
LF, ENV, FEES, HEDGE, GST = 1.034, 1.781, 0.157, 0.263, 0.10
COMP = [("Spot", "#E8731A"), ("Losses (x1.034)", "#F2B27A"), ("Network", "#6B6661"),
        ("Certificates", "#2E8B57"), ("Market fees", "#CFCAC4"), ("Hedging", "#4C6A92"), ("GST", "#231F20")]
plt.rcParams.update({"font.family": ["Lato", "DejaVu Sans"], "font.size": 7.5, "text.color": "#231F20",
                     "axes.edgecolor": "#CFCAC4", "xtick.color": "#231F20", "ytick.color": "#231F20"})
fig, ax = plt.subplots(figsize=(16 / 2.54, 6.2 / 2.54), dpi=300)
rows = list(SPOT)[::-1]
for y, k in enumerate(rows):
    sub = SPOT[k] * LF + NET[k] + ENV + FEES + HEDGE
    vals = [SPOT[k], SPOT[k] * (LF - 1), NET[k], ENV, FEES, HEDGE, sub * GST]
    left = 0
    for (name, col), v in zip(COMP, vals):
        ax.barh(y, v, left=left, color=col, height=0.62, label=name if y == 0 else None, edgecolor="white", linewidth=0.4)
        if v > 1.2: ax.text(left + v / 2, y, f"{v:.1f}", ha="center", va="center", fontsize=6.3,
                            color="white" if col in ("#6B6661", "#231F20", "#4C6A92", "#2E8B57", "#E8731A") else "#231F20")
        left += v
    ax.text(left + 0.4, y, f"{left:.1f} c", va="center", fontsize=7, weight="bold")
    if k in TOU:
        ax.plot([TOU[k]] * 2, [y - 0.38, y + 0.38], color="#00857C", lw=1.6)
        ax.text(TOU[k], y + 0.43, f"ToU {TOU[k]} c", color="#00857C", fontsize=6.2, ha="center", va="bottom")
ax.set_yticks(range(len(rows))); ax.set_yticklabels(rows)
ax.set_xlabel("Average import price, 2023 (c/kWh)"); ax.set_xlim(0, 44)
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.legend(ncol=7, loc="upper center", bbox_to_anchor=(0.45, -0.28), frameon=False, fontsize=6.3, handlelength=1.2, columnspacing=1.0)
fig.tight_layout()
fig.savefig(sys.argv[1], dpi=300, facecolor="white")
print("saved", sys.argv[1])
