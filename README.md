# FIN 4600 — Lab 3: Financial Data Analytics

**Michigan Technological University · College of Business**

A hands-on lab that takes you from raw market and credit data to working
machine learning models, using Python, pandas and scikit-learn.

Built as applied material for **Chapter 6, "Data Analytics"** of Randall E.
Duran, *Financial Services Technology: Processes, Architecture, and Solutions*
(3rd edition). See [`DURAN_CH6_CROSSWALK.md`](DURAN_CH6_CROSSWALK.md) for the
mapping.

---

## Start here

**New to this? Read [`SETUP.md`](SETUP.md) first.** It walks through GitHub,
VS Code, and the Python environment step by step, and it has a troubleshooting
section for when something goes wrong.

If you already have `uv` installed:

```bash
git clone <your fork's URL>
cd mtu4600-lab3-analytics
uv sync
```

Then open the folder in VS Code and run
`notebooks/00_environment_check.ipynb`.

---

## The notebooks

Work through them in order. Each builds on the one before.

| # | Notebook | What you do | Time |
|---|---|---|---|
| 00 | **Environment check** | Confirm Python, packages and data all work | 15 min |
| 01 | **pandas fundamentals** | Load, filter, group, pivot, resample, join and clean real market data | 75 min |
| 02 | **Returns and risk** | Returns, volatility, Sharpe, drawdown, correlation, fat tails, VaR, beta | 75 min |
| 03 | **Features and targets** | Build a modelling table — and learn to spot look-ahead bias | 60 min |
| 04 | **Credit risk ML** | A full credit-scoring workflow ending in a profit-based approval rule | 90 min |
| 05 | **Market prediction ML** | Apply the same models to markets, and learn to read a null result | 60 min |

Every notebook ends with exercises. They are the part that teaches.

---

## What you will be able to do afterwards

- Load a vendor data file and find its problems before they find you
- Compute the risk and performance measures a desk actually reports
- Build a feature table from a time series without leaking the future into it
- Fit, tune and — most importantly — *honestly evaluate* a classifier
- Explain why a credit model in production is usually a logistic regression
- Turn a model's probability into a business decision using expected profit
- Recognise when a result is too good to be true, and go looking for the bug

---

## The data

Five real datasets, committed to the repository so that everyone gets identical
results and nothing breaks when a free API changes.

| File | What it is |
|---|---|
| `sp500_prices.csv` | Daily OHLCV for 30 large-cap US stocks, 2013–2018 |
| `sp500_companies.csv` | Security master: ticker, company, GICS sector |
| `vix_daily.csv` | CBOE Volatility Index, 2012–2018 |
| `us10y_monthly.csv` | US 10-year Treasury yield, monthly since 1990 |
| `german_credit.csv` | 1,000 consumer loan applications with known outcomes |

Full data dictionary, sources, and the known limitations of each file:
[`data/README.md`](data/README.md).

The limitations are worth reading. The price data is not dividend-adjusted and
is survivorship-biased, and the notebooks say so where it matters.

---

## Repository layout

```
mtu4600-lab3-analytics/
├── SETUP.md                    Start here — GitHub, VS Code, Python
├── INSTRUCTOR_NOTES.md         Teaching notes, timings, grading
├── DURAN_CH6_CROSSWALK.md      Mapping to the textbook chapter
├── pyproject.toml              Dependencies
├── uv.lock                     Exact versions — do not delete
├── fin4600.mplstyle            Shared chart style
├── data/                       Committed datasets + data dictionary
│   └── processed/              Written by the notebooks (not in Git)
├── notebooks/                  The six labs
└── scripts/
    ├── check_environment.py    Terminal version of notebook 00
    ├── refresh_data.py         Optional live data download
    └── run_all_notebooks.py    Execute everything (instructor/CI)
```

---

## Requirements

- Any computer running Windows, macOS or Linux
- About 1 GB of free disk space
- No prior Python installation needed — `uv` handles it

Built and tested on Python 3.12 with pandas 3.0, scikit-learn 1.9 and
matplotlib 3.11.

---

## A note on what this lab teaches

Most introductory financial-ML material shows you a model that appears to beat
the market, because the author did not lag a feature properly. This lab does
the opposite: it teaches the discipline that catches those mistakes, and then
demonstrates a genuine null result rather than hiding it.

Notebook 04 shows machine learning working well, on credit risk, where the
signal is real. Notebook 05 shows it failing on price direction, where it
should fail — and then succeeding modestly on volatility, where the signal is
weaker than a textbook promises but stronger than nothing. Understanding why
those three outcomes differ is the point of the whole lab.

---

## Licence and attribution

Course material for Michigan Technological University FIN 4600.

Data files retain the licences of their original sources, which are listed in
[`data/README.md`](data/README.md). The Statlog (German Credit) dataset is
credited to Professor Dr. Hans Hofmann, Universität Hamburg, and distributed
through the UCI Machine Learning Repository.
