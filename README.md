## Data Science Project: Identifying Periods of Corporate Credit Stress

### Project Overview
Periods when corporate loan defaults increase are important signals of financial stress, as they indicate pressure on firms and a higher likelihood of losses for banks. However, financial stress cannot be observed directly. Instead, it must be inferred from indicators and assessed for materiality.

This project analyses UK corporate credit stress using publicly available survey‑based indicators from the Bank of England (BoE). In particular, it focuses on lender‑reported changes in default rates on loans to medium and large private non‑financial corporations (PNFCs). UK government bond yields are included to provide additional context on broader financial conditions over the same periods.

The analysis is designed to be transparent, reproducible, and easy to interpret, and was carried out as part of a Level 6 Data Science project.

---

### Objectives
The main objectives of the project are to:

- Identify periods of sustained increases in reported corporate loan defaults
- Assess whether stress patterns differ between medium and large firms
- Compare survey‑based stress indicators with known macro‑financial events
- Provide an external benchmark for internal, market‑based stress analysis

---

### Data Sources
The analysis is based entirely on publicly available data:

- **Bank of England Credit Conditions Survey (CCS)**  
  Quarterly survey results reporting net balances of lenders indicating whether default rates have increased or decreased compared to the previous quarter.

- **UK Government Bond Yields**  
  Daily nominal government liability curve data published by the Bank of England, used to provide broader financial market context.

All data is aggregated and does not contain any personal or firm‑level information.

---

### Data Engineering
The data engineering work focused on transforming multiple raw datasets with different structures into a single, reliable quarterly time series suitable for analysis.

The CCS data is published as a wide Excel file rather than a ready‑to‑use time series. Relevant rows corresponding to reported changes in default rates for medium and large PNFCs were extracted directly. Year and quarter labels were reconstructed from survey headers and combined into standard quarterly date labels. Validation checks were applied to ensure no observations were dropped unintentionally.

Government bond yield data was sourced from multiple Excel files, each covering different historical periods and reported at a daily frequency. A consistent maturity was extracted from each file, the datasets were combined into a single continuous series, and dates were standardised. Daily yields were aggregated into quarterly averages to align with the CCS reporting frequency.

The survey and yield datasets were then merged using quarterly labels, with the survey data treated as the primary dataset. A left join was intentionally used to ensure that all survey observations were retained, even in periods where yield data was unavailable.

To reduce short‑term volatility and focus on sustained developments, four‑quarter moving averages were calculated for both default rate indicators and government bond yields.

All intermediate datasets and the final analytical output were saved separately to ensure traceability and reproducibility.

---

### Methodology
The Credit Conditions Survey reports net percentage balances, where a positive value indicates that more lenders reported defaults increasing rather than decreasing. As this is a survey‑based indicator, it reflects lenders’ judgement and experience rather than realised loan‑level default data.

Medium and large PNFCs are analysed separately, as firms of different sizes can experience financial stress in different ways. Combining the two groups could obscure meaningful differences in stress dynamics.

A four‑quarter moving average was applied to both series to avoid over‑reacting to one‑off quarterly movements. This smoothing technique helps highlight sustained stress periods rather than short‑lived spikes, making the results more relevant from a risk management perspective.

---

### Key Findings
The most severe and prolonged period of default stress occurs between **2008 and 2009**, corresponding to the Global Financial Crisis. This episode stands out clearly once the moving averages are applied.

Later periods show renewed increases in reported default pressure, but these episodes are generally smaller in magnitude and shorter in duration. Medium and large PNFCs move broadly in the same direction over time, although stress appears slightly more pronounced for medium‑sized firms.

Movements in government bond yields broadly align with major changes in the financial environment, providing useful contextual background. However, the analysis does not assume a direct causal relationship between interest rates and default behaviour.

---

### Visualisation
The results are presented using simple time‑series charts rather than complex dashboards. Separate charts are used for medium and large PNFCs, each showing both raw survey values and their smoothed moving averages.

This approach avoids overcrowding and makes it easier to compare stress patterns across firm sizes. Consistent time axes and colour schemes are used throughout to support interpretability.

The visualisations make it clear when default pressure intensifies, how long stress episodes persist, and how patterns differ across firm segments.

---

### Tools and Technologies
- Python  
- pandas (data manipulation and time‑series analysis)  
- Excel (validation and review of outputs)

The full Python implementation is available in this repository.

---

### Ethical, Legal and Practical Considerations
The project uses only publicly available and aggregated data. There are no personal data, company‑specific records or GDPR considerations.

The primary limitation of the analysis is its reliance on survey responses, which may be influenced by lender sentiment or timing effects. For this reason, results are interpreted cautiously, and all modelling choices and assumptions are clearly documented to support transparency and good governance.

---

### Relation to Internal Risk Analysis
This project was carried out to provide an external point of comparison with internal analysis based on traded market data. Internal work identifies stressed periods using five‑year credit spread curves and exposure‑weighted counterparty information.

Comparing the two approaches helps distinguish between:
- Stress that is specific to traded counterparties and markets
- Stress that is more widespread across the broader corporate sector

This strengthens confidence in periods identified as genuinely systemic rather than portfolio‑specific.
