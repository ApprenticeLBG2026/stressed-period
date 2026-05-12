import pandas as pd


ccs_data = pd.read_excel(r"ccs-2026-q1-annex.xlsx", sheet_name="Corporate annex", header=None)
yield_data_2005_2015 = pd.read_excel(r"GLC Nominal daily data_2005 to 2015.xlsx", sheet_name="4. spot curve", header=None)
yield_data_2016_2024 = pd.read_excel(r"GLC Nominal daily data_2016 to 2024.xlsx", sheet_name="4. spot curve", header=None)
yield_data_2025_present = pd.read_excel(rGLC Nominal daily data_2025 to present.xlsx", sheet_name="4. spot curve", header=None)


years = ccs_data.iloc[15, 2:]
quarters = ccs_data.iloc[16, 2:]
medium_pnfc = ccs_data.iloc[83, 2:]
large_pnfc = ccs_data.iloc[86, 2:]

years = years.ffill()
labels = quarters.astype(str) + " " + years.astype(int).astype(str)

default_rate_change = pd.DataFrame({
    "date": labels,
    "medium pnfc default rate change": medium_pnfc.values,
    "large pnfc default rate change": large_pnfc.values
}).dropna().reset_index(drop=True)

def extract_5y(df):

    out = pd.DataFrame({
        "date": df.iloc[5:, 0],   # column A, from row 6
        "5y": df.iloc[5:, 10]     # column K, from row 6
    })

    out["date"] = pd.to_datetime(out["date"], errors="coerce")
    return out.dropna()


yield_5y_2005_2015 = extract_5y(yield_data_2005_2015)
yield_5y_2016_2024 = extract_5y(yield_data_2016_2024)
yield_5y_2025_present = extract_5y(yield_data_2025_present)


yield_5y_all = (
    pd.concat(
        [yield_5y_2005_2015, yield_5y_2016_2024, yield_5y_2025_present],
        ignore_index=True
    )
    .sort_values("date")
    .reset_index(drop=True)
)
yield_5y_all = yield_5y_all.sort_values("date")


yield_5y_q = (
    yield_5y_all
    .set_index("date")["5y"]
    .resample("Q")
    .mean()
    .reset_index()
)

yield_5y_q["date"] = (
    "Q" + yield_5y_q["date"].dt.quarter.astype(str)
    + " " + yield_5y_q["date"].dt.year.astype(str)
)


#chose left joint to be able to detect nans in the 5y coumn
check_q = default_rate_change.merge(
    yield_5y_q,
    on="date",
    how="left"
)

missing = check_q[check_q["5y"].isna()]


check_q["medium_pnfc_ma4"] = (
    check_q["medium pnfc default rate change"]
    .rolling(window=4, min_periods=4)
    .mean()
)

check_q["large_pnfc_ma4"] = (
    check_q["large pnfc default rate change"]
    .rolling(window=4, min_periods=4)
    .mean()
)


check_q["5y_yield_ma4"] = (
    check_q["5y"]
    .rolling(window=4, min_periods=4)
    .mean()
)

check_q.to_excel(r"\\cmdfs\DFS-LDN-DATA\Risk\Market Risk Management 2\Model Validation\FORM\Nas\Level 6 Data Science apprenticeship\DSPP\ccs_and_yield_timeseries.xlsx", index=False)

print('hi')
