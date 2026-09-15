# Data dictionary and provenance

All files in this folder are **real data**, committed to the repository on
purpose. See `scripts/refresh_data.py` for the reasoning and for an optional
live-download path.

Files written by the notebooks land in `data/processed/` and are ignored by
Git — they are rebuilt by running the notebooks in order.

---

## `sp500_prices.csv`

Daily open/high/low/close/volume for 30 large-cap US stocks.

| Column | Type | Description |
|---|---|---|
| `date` | date | Trading date (ISO format) |
| `ticker` | text | Exchange ticker symbol |
| `open` | float | Opening price, USD |
| `high` | float | Session high, USD |
| `low` | float | Session low, USD |
| `close` | float | Closing price, USD |
| `volume` | integer | Shares traded |

- **Rows:** 37,770 (30 tickers × 1,259 trading days)
- **Period:** 2013-02-08 to 2018-02-07
- **Missing values:** none
- **Source:** the `all_stocks_5yr` S&P 500 daily dataset as mirrored in the
  [plotly/datasets](https://github.com/plotly/datasets) repository, subset to
  30 tickers chosen for sector diversity and name recognition.

**Two things to know before you use these prices for anything serious.**

1. **They are not adjusted for dividends.** Total return is therefore
   understated, most visibly for high-yield names such as T, VZ, XOM and DUK.
   The notebooks say so where it matters.
2. **They are survivorship-biased.** The 30 tickers are companies that were in
   the index in 2018. Firms that were acquired, delisted or collapsed during
   2013–2018 are absent. Any backtest built on this file will look better than
   reality, and that is worth remembering every time you read a published
   backtest.

## `sp500_companies.csv`

A small security master: reference attributes for each ticker.

| Column | Type | Description |
|---|---|---|
| `ticker` | text | Exchange ticker symbol — the join key |
| `company` | text | Company name |
| `sector` | text | GICS sector |
| `sub_industry` | text | GICS sub-industry |
| `headquarters` | text | Headquarters location |
| `date_added` | date | Date added to the S&P 500 |
| `cik` | integer | SEC Central Index Key |

- **Rows:** 100 — the 30 tickers in the price file plus 70 others, so that
  joins behave realistically rather than as a perfect one-to-one match
- **Source:** [datasets/s-and-p-500-companies](https://github.com/datasets/s-and-p-500-companies),
  derived from the Wikipedia constituent list

**Note:** this is a *current* membership list while the prices cover 2013–2018.
Notebook 01 uses that mismatch deliberately to teach what a careless inner join
does to a risk report.

## `vix_daily.csv`

The CBOE Volatility Index — the options market's 30-day forward-looking
estimate of S&P 500 volatility, quoted as an annualised percentage.

| Column | Type | Description |
|---|---|---|
| `date` | date | Trading date |
| `vix_open` | float | Opening level |
| `vix_high` | float | Session high |
| `vix_low` | float | Session low |
| `vix_close` | float | Closing level |

- **Rows:** 1,760
- **Period:** 2012-01-03 to 2018-12-31 (deliberately wider than the price file,
  so rolling windows have history at the start of the sample)
- **Source:** [datasets/finance-vix](https://github.com/datasets/finance-vix),
  sourced from CBOE

## `us10y_monthly.csv`

US 10-year Treasury constant-maturity yield, monthly.

| Column | Type | Description |
|---|---|---|
| `date` | date | First day of the month |
| `yield_pct` | float | Yield in percent (2.83 means 2.83%) |

- **Rows:** 439
- **Period:** 1990-01 to 2026-07
- **Source:** [datasets/bond-yields-us-10y](https://github.com/datasets/bond-yields-us-10y),
  derived from US Treasury data

Used in Notebook 02 as a stand-in for the risk-free rate. A correct Sharpe
ratio uses a *short* rate (3-month bills); the notebook flags the approximation
rather than hiding it.

## `german_credit.csv`

The Statlog (German Credit) dataset — 1,000 consumer loan applications with
known outcomes. A teaching and benchmarking standard since 1994.

| Column | Type | Description |
|---|---|---|
| `applicant_id` | text | Synthetic identifier added for this lab |
| `status` | text | Status of the existing checking account |
| `duration` | integer | Loan duration in months |
| `credit_history` | text | Past repayment behaviour |
| `purpose` | text | Purpose of the loan |
| `amount` | integer | Credit amount, Deutsche Marks |
| `savings` | text | Savings account / bonds balance band |
| `employment_duration` | text | Years in present employment |
| `installment_rate` | integer | Instalment as a percentage of disposable income (1–4 band) |
| `personal_status_sex` | text | Sex and marital status — **protected attribute** |
| `other_debtors` | text | Co-applicant or guarantor |
| `present_residence` | integer | Years at present address (1–4 band) |
| `property` | text | Most valuable available asset |
| `age` | integer | Applicant age in years |
| `other_installment_plans` | text | Other instalment plans held |
| `housing` | text | Rent, own, or free |
| `number_credits` | integer | Existing credits at this bank |
| `job` | text | Employment category |
| `people_liable` | integer | Dependants |
| `telephone` | text | Telephone registered |
| `foreign_worker` | text | Foreign worker — **protected attribute** |
| `default` | integer | **Target.** 1 = bad credit risk, 0 = good |

- **Rows:** 1,000
- **Default rate:** 30.0%
- **Original source:** Professor Dr. Hans Hofmann, Universität Hamburg;
  distributed through the UCI Machine Learning Repository as *Statlog (German
  Credit Data)*
- **This copy:** the readable-label variant mirrored at
  [selva86/datasets](https://github.com/selva86/datasets)

**Recoding applied for this lab.** The source file carries `credit_risk`, where
1 means a good risk. That was inverted to `default`, where **1 means the loan
went bad**, so that the positive class is the event of interest — which is the
credit-risk convention and makes precision and recall read the right way round.
An `applicant_id` column was added.

**Label caveat.** The category labels in this variant differ in places from the
original UCI codebook — the first checking-account band reads "... < 100 DM"
here where UCI documents A11 as a negative balance. Use the labels as given and
do not attach economic interpretation to the exact thresholds.

**Fair lending.** `personal_status_sex` and `foreign_worker` are protected or
protected-adjacent characteristics, and `age` is protected under the US Equal
Credit Opportunity Act for applicants of contracting age. Notebook 04 treats
this as a first-class topic rather than a footnote. The dataset is a teaching
artefact from 1994 German consumer lending; it is not a template for a model
you would deploy.
