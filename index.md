# Stressed Period Identification for IRC

This project automates the identification of credit‑stressed periods to support
Internal Model Method (IMM) calibration for the Incremental Risk Charge (IRC).

The aim was to replace a largely manual, spreadsheet‑based process with a
reproducible Python workflow.

---

## Business context

Under CRR Article 284(4), stressed inputs used in IRC calibration must be based
on an appropriate historical stress period.

Previously, identifying this period involved manual data pulls, ad‑hoc
weighting, and judgement‑led comparisons. This made the process time‑consuming,
hard to reproduce, and difficult to justify to audit.

---

## What this project does

The pipeline:

- Ingests daily PD time series by issuer / ticker  
- Merges exposure data to compute exposure‑weighted risk measures  
- Calculates alternative stress metrics across time  
- Produces plots and summary tables to support stressed‑period selection  

The code is designed to be rerun quarterly or on request, using updated inputs.

---

## Key outputs

![Stressed period metrics](assets/stressed_period_plot.png)

The outputs allow different stress definitions to be compared consistently,
rather than relying on a single headline measure.

---

## Repository structure

- `src/` – core Python pipeline  
- `analysis/` – exploratory and validation notebooks  
- `outputs/` – generated tables and plots  
- `assets/` – figures used on this site  

---

## Code and analysis

- Core pipeline: src/  
- Main analysis notebook: analysis/stressed_period.ipynb  
