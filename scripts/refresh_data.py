"""Optionally refresh the bundled price data from a live market data feed.

    uv sync --extra live
    uv run python scripts/refresh_data.py --help

WHY THE REPOSITORY SHIPS STATIC CSVs
------------------------------------
The files in data/ are committed on purpose:

* every student gets identical numbers, so a disagreement is a code problem
  rather than a data problem;
* the labs work offline, behind a campus firewall, and on exam day;
* nothing breaks when a free data provider changes its API, which they do.

This script exists so you can see how the data would be collected in practice,
and so the repository can be brought forward to a more recent period. It is not
needed for any of the notebooks.

CAVEAT
------
yfinance scrapes an undocumented Yahoo Finance endpoint. It breaks periodically,
it rate-limits, and it is not licensed for commercial use. It is fine for
coursework and wrong for anything that matters. A production system buys data
from a vendor with a contract and a support line.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

DEFAULT_TICKERS = [
    "AAPL", "AMT", "BA", "BAC", "CAT", "CSCO", "CVX", "DIS", "DUK", "GE",
    "GOOGL", "GS", "HD", "INTC", "JNJ", "JPM", "KO", "MCD", "MMM", "MSFT",
    "NEE", "NKE", "PFE", "PG", "T", "UNH", "VZ", "WFC", "WMT", "XOM",
]


def find_repo_root() -> Path:
    here = Path(__file__).resolve()
    for candidate in [here.parent, *here.parents]:
        if (candidate / "data").is_dir():
            return candidate
    raise SystemExit("Could not find the repository root.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", default="2013-02-08", help="first date (YYYY-MM-DD)")
    parser.add_argument("--end", default="2018-02-08", help="last date (YYYY-MM-DD)")
    parser.add_argument("--tickers", nargs="*", default=DEFAULT_TICKERS)
    parser.add_argument(
        "--output",
        default="data/processed/sp500_prices_live.csv",
        help="where to write; defaults to a NEW file so the bundled data is not overwritten",
    )
    args = parser.parse_args()

    try:
        import pandas as pd
        import yfinance as yf
    except ImportError:
        print(
            "yfinance is not installed. It is an optional extra:\n"
            "    uv sync --extra live",
            file=sys.stderr,
        )
        return 1

    print(f"Requesting {len(args.tickers)} tickers from {args.start} to {args.end}...")
    raw = yf.download(
        args.tickers,
        start=args.start,
        end=args.end,
        auto_adjust=True,
        progress=False,
        group_by="column",
    )

    if raw.empty:
        print(
            "No data came back. Yahoo may be rate-limiting you, the endpoint may\n"
            "have changed, or your network may block it. This is exactly why the\n"
            "repository ships static CSVs. Nothing else in the labs is affected.",
            file=sys.stderr,
        )
        return 1

    # yfinance returns a wide frame with a (field, ticker) column MultiIndex.
    # Reshape it into the long format the notebooks expect.
    frames = []
    for field, name in [
        ("Open", "open"),
        ("High", "high"),
        ("Low", "low"),
        ("Close", "close"),
        ("Volume", "volume"),
    ]:
        block = raw[field].stack().rename(name)
        frames.append(block)

    long = pd.concat(frames, axis=1).reset_index()
    long.columns = ["date", "ticker", "open", "high", "low", "close", "volume"]
    long = long.dropna(subset=["close"]).sort_values(["ticker", "date"])

    repo = find_repo_root()
    destination = repo / args.output
    destination.parent.mkdir(parents=True, exist_ok=True)
    long.to_csv(destination, index=False)

    print(f"Wrote {len(long):,} rows to {destination}")
    print(f"Tickers: {long['ticker'].nunique()}   "
          f"Dates: {long['date'].min().date()} to {long['date'].max().date()}")
    print(
        "\nNOTE: prices here are split- and dividend-adjusted (auto_adjust=True),\n"
        "so they will NOT match data/sp500_prices.csv exactly. Adjusted series\n"
        "also change retroactively whenever a new dividend is paid, which is a\n"
        "reproducibility problem worth understanding before you rely on them."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
