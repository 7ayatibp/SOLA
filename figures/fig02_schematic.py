"""Report Figure 2: perfect-foresight benchmark vs rolling-horizon controller. Usage: python schematic.py out.png"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

INK, GREY, LIGHT, TINT, YEL = "#231F20", "#6B6661", "#CFCAC4", "#F4F2EE", "#FFE600"
plt.rcParams.update({"font.family": ["Lato", "Inter", "DejaVu Sans"], "font.size": 7.5, "text.color": INK})

W, H = 16.0, 6.6                                   # cm, printed size
fig = plt.figure(figsize=(W / 2.54, H / 2.54), dpi=300)
ax = fig.add_axes([0, 0, 1, 1]); ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")


def box(x, y, w, h, title, body, accent):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.12", fc=TINT, ec="none", zorder=2))
    ax.add_patch(Rectangle((x, y + h - 0.07), w, 0.07, fc=accent, ec="none", zorder=3))
    ax.text(x + 0.15, y + h - 0.22, title, weight="bold", va="top", fontsize=7.5, zorder=4)
    ax.text(x + 0.15, y + h - 0.6, body, va="top", fontsize=6.3, color=GREY, linespacing=1.3, zorder=4)


def arrow(x0, y0, x1, y1):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>", mutation_scale=7,
                                 lw=0.9, color=INK, shrinkA=0, shrinkB=0, zorder=5))


def row(y, h, items, accent):
    for x, (t, b) in zip(XS, items):
        box(x, y, BW, h, t, b, accent)
    for x in XS[:-1]:
        arrow(x + BW + 0.06, y + h / 2, x + BW + GAP - 0.06, y + h / 2)


XS, BW, GAP = [0.3, 4.3, 8.3, 12.3], 3.4, 0.6

ax.text(0.3, 6.37, "Benchmark: perfect foresight (Part 7)", weight="bold", fontsize=8, va="center")
row(4.66, 1.44, [("Inputs", "Actual load, PV and prices,\none week at a time"),
                ("Optimise", "One LP per week at 5-min\nsteps (linprog, HiGHS)"),
                ("Dispatch", "Battery follows the\nplan exactly"),
                ("Settle", "Bill on actual prices,\nPV and load")], LIGHT)

ax.text(0.3, 4.2, "VPP-SPREE controller: rolling horizon (Part 11)", weight="bold", fontsize=8, va="center")
y2, h2 = 1.95, 1.9
row(y2, h2, [("1  Forecast at hour τ", "PV (Task 9.1) and spot price\n(Task 10.1); load known;\nflat and ToU prices fixed"),
             ("2  Plan next 48 h", "Same LP at hourly steps,\nfrom the battery's actual\nstate of charge"),
             ("3  Execute one hour", "Follow the first-hour setpoint\nfor 12 × 5-min intervals,\nblind to their price and PV"),
             ("4  Settle", "Bill on actual 5-min\nprices, PV and load")], YEL)

xl, xr, yb = XS[0] + BW / 2, XS[2] + BW / 2, y2 - 0.38
ax.plot([xr, xr, xl], [y2, yb, yb], color=INK, lw=0.9, zorder=5)
arrow(xl, yb, xl, y2 - 0.02)
ax.text((xl + xr) / 2, yb - 0.08, "τ + 1 h: re-plan with new forecasts (8,760 plans a year)",
        ha="center", va="top", fontsize=6.4, color=GREY)

y3, hs, x0, x1 = 0.42, 0.3, 3.2, 15.7
cw = (x1 - x0) / 48
for k in range(48):
    ax.add_patch(Rectangle((x0 + k * cw, y3), cw * 0.92, hs, fc=INK if k == 0 else LIGHT, ec="none"))
ax.text(x0 - 0.15, y3 + hs / 2, "Plan made at τ", ha="right", va="center", fontsize=6.6, weight="bold")
ax.text(x0, y3 - 0.08, "τ", va="top", fontsize=6.2, color=GREY)
ax.text((x0 + x1) / 2, y3 - 0.08, "hour 1 executed (black); hours 2-48 planned, then replaced by the next plan",
        ha="center", va="top", fontsize=6.2, color=GREY)
ax.text(x1, y3 - 0.08, "τ + 48 h", ha="right", va="top", fontsize=6.2, color=GREY)

fig.savefig(sys.argv[1], dpi=300, facecolor="white")
print("saved", sys.argv[1])
