# SOLA4237 Assignment 2: household battery optimisation (site 23W0158, Thredbo NSW)

All analysis behind the report *Household battery optimisation and VPP value assessment*:
data checks and cleaning, tariffs, battery model, perfect-foresight optimiser, sizing,
PV and price forecasts, a 48-hour rolling-horizon scheduler, the PV-vs-price ablation,
sensitivity tests and techno-economics.

## Contents
| Path | What it is |
|---|---|
| `SOLA4237_Assignment2.ipynb` | The notebook: Parts 0-14, Appendix B (reproducibility), Appendix C (report figures) |
| `AI_LOG.md` | Row-by-row log of every AI use and how it was checked (source of the report's AI disclosure) |
| `Data_NSW_Thredbo - Alpine_2022-2023_partial.csv` | Site data supplied with the assignment (5-minute, 2022-2023) |
| `data/` | AEMO NSW1 spot prices (downloaded once by Part 3) and cached results in `data/results/` |
| `figures/` | Report figure exports (`figures/report/`) and the method schematic script |
| `requirements.txt` | Package versions used |

## Run it
```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook SOLA4237_Assignment2.ipynb   # or open it in VS Code
```
Then **Restart & Run All**. It takes a few minutes because the slow results (sizing sweep,
rolling-horizon runs, sensitivity runs) reload from `data/results/`. Every cached result is keyed
by a hash of its inputs, so changing an input recomputes it rather than reusing a stale file.
To force a group to recompute, set its flag in Part 0 or at the top of its Part
(`RERUN_SWEEP`, `RERUN_ROLLING`, `RERUN_SENS`, `RERUN_2022`, `RERUN_V2`); a full recompute
takes about an hour.

## How the notebook is organised
Each task follows one pattern: background -> decision -> function -> test -> apply to site data ->
finding. 29 test cells (154 assertions) check every function on small hand-calculated or synthetic
cases before it touches site data, and reconciliation asserts check that Parts 7, 12 and 14 agree.
The 25 findings (blockquotes) are the source for every claim in the report.

## AI use
AI (Claude) was used at UNSW Level 4 (assistance with attribution). Every use is logged in
`AI_LOG.md` with what the AI did, who wrote what, and how it was verified.
