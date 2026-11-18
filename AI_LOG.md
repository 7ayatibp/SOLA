# AI Use Log: SOLA4237 Assignment 2

Running record of how AI (Claude) was used, and how each output was checked.
Course AI level: **4, assistance with attribution**. From 18 Nov, Claude writes more code directly, and every item is attributed here.
Source material for **Appendix A: AI disclosure** (worth 40% of the 25-mark appendix).
Add an entry every session. The disclosure is written from this log at the end.

**Who did what:** **AI** = AI wrote it · **Me** = I wrote it · **AI review** = I wrote it, AI reviewed it or fixed it

| Date | Part / task | What AI did | Who | How I checked it / what I changed | Status |
|---|---|---|---|---|---|
| Oct 2026 | Whole notebook | Generated a notebook skeleton (Part 0-15 structure, status table, requirements tracker) | AI | Chose to rebuild each task myself step by step with a small test per task, rather than run the skeleton as-is | Done |
| Oct-Nov 2026 | Part 0, Tasks 1.1-1.5 | (Built by me on the skeleton's structure) | Me | Own tests in every task; findings 1.2-1.3 written by me | Done |
| 15 Nov 2026 | Whole assignment | Read brief, rubric and notebook; summarised progress; suggested Part 1 fixes and Part 2 questions | AI | Used as a checklist, not as content | Done |
| 15 Nov 2026 | Finding 1.4 | Wrote the "so what for the battery" paragraph and a new cell giving the value of one shifted kWh per tariff; deleted a scratch cell and a duplicate tariff print | AI | TODO: re-run and confirm the 2.6 kWh/day peak-window figure; add evidence from the min/max table (whole-hour windows, no seasonal change, weekday = weekend), window lengths and a pointer to the wholesale tariff in Part 3 | To verify |
| 15 Nov 2026 | Finding 1.5 | Wrote the finding text and a weekday check cell (2022 starts on a Saturday, 2023 on a Sunday) | AI | TODO: re-run and confirm the weekday range (28.2-29.8 kWh/day) | To verify |
| 15 Nov 2026 | Part 2 (first attempt) | Drafted all of Part 2 (functions, tests, findings) | AI | **Rolled it back** and chose to write Part 2 myself with hints, so I understand and can defend it | Rejected |
| 15 Nov 2026 | Notebook structure | Agreed with my proposal: Part 1 = diagnose (spurious-data checks become Task 1.6), Part 2 = fix only | Me | My idea; AI confirmed it fits the brief's "identify, then clean with justification" | Done |
| 15 Nov 2026 | Task 1.6 quality_report | Reviewed my function (adapted from my Assignment 1 Task 2.2). Found 2 bugs: (1) price bounds in $/MWh but the column is $/kWh, so the check could never fail; (2) `if col["solar"] in df` is always True, so Year 2 commercial PV was never checked. Wrote the fixed version: PV column and capacity as arguments, a capacity check, a consistent 0.01 kW tolerance | AI review | AI ran it on the site data: Y1 checks 104,936 PV rows, Y2 checks 105,120, so Year 2 is now tested. Function in notebook; all checks pass on both years. Leftover change comments removed 18 Nov | Done |
| 15 Nov 2026 | Task 1.6 markdown | Drafted the task heading and background cell (three kinds of check; why cross-sensor checks are the strongest) | AI | TODO: edit into my own words; make sure each check named matches the final function | To verify |
| 18 Nov 2026 | Task 1.6 tests | Wrote the test cell: synthetic frame with one of each fault, a Year 2-shaped frame (measured PV all NaN) proving the forecast is checked, and a check that an empty PV column is skipped rather than reported as zeros | AI | Ran on my notebook: passes. TODO: read through and confirm each assert matches the check it tests | To verify |
| 18 Nov 2026 | Task 1.6 ratio | Wrote `daily_pv_irr_ratio` plus its test. **Caught an error in the approach:** on days with an irradiance outage the ratio is inflated (infinite on 2 Jul 2023), so it now uses complete days only | AI | Ran on site data: Y1 6.95-8.09 (median 7.57), Y2 7.29-8.12 (median 7.72). TODO: sanity-check against the system size in Part 4 | To verify |
| 18 Nov 2026 | Task 1.6 temperature runs | Wrote `longest_run_details` to locate the longest constant runs | AI | Both are overnight in winter (24 Aug 2022, -0.8 C; 5 Jul 2023, 4.2 C), so judged a calm night, not a stuck sensor. TODO: I should agree with that judgement | To verify |
| 18 Nov 2026 | Task 1.6 irradiance resolution | Wrote the check showing 5-min irradiance is hourly data interpolated (equal steps in 100% of daylight hours) | AI | Ran on site data. Carries forward as a caveat for the Part 9 PV model | To verify |
| 18 Nov 2026 | Finding 1.6 and Part 1 summary | Wrote Finding 1.6 and the Part 1 summary table (issues -> next step); updated the status table | AI | TODO: edit into my own words; check every number against the cell outputs | To verify |

## Disclosure draft
_To be written at the end from the table above. Keep in mind:_
- _how AI was used: skeleton, review, debugging, drafting text_
- _what was rejected and why (the Part 2 rollback is strong evidence of judgement)_
- _errors AI made or caught (the unit bug, the always-true condition)_
- _how every AI output was verified (tests, re-running on data, cross-checks against the brief)_
