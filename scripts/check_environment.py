"""Verify the lab environment from the command line.

Run with:

    uv run python scripts/check_environment.py

This is the terminal equivalent of notebooks/00_environment_check.ipynb. It is
useful when a notebook will not start and you need to find out whether the
problem is the environment or the notebook kernel.
"""

from __future__ import annotations

import sys
from pathlib import Path

REQUIRED = [
    ("numpy", "2.0"),
    ("pandas", "2.2"),
    ("matplotlib", "3.8"),
    ("seaborn", "0.13"),
    ("sklearn", "1.5"),
    ("scipy", "1.11"),
]

EXPECTED_DATA_FILES = [
    "sp500_prices.csv",
    "sp500_companies.csv",
    "vix_daily.csv",
    "us10y_monthly.csv",
    "german_credit.csv",
]


def find_repo_root() -> Path:
    here = Path(__file__).resolve()
    for candidate in [here.parent, *here.parents]:
        if (candidate / "data" / "sp500_prices.csv").exists():
            return candidate
    raise SystemExit(
        "Could not find the repository root.\n"
        "Run this from inside the mtu4600-lab3-analytics folder."
    )


def check_interpreter() -> bool:
    print("1. Python interpreter")
    print(f"   {sys.executable}")
    print(f"   version {sys.version.split()[0]}")

    if ".venv" in sys.executable:
        print("   OK - running the project virtual environment\n")
        return True

    print(
        "   WARNING - this is not the project's .venv.\n"
        "   Run this script as:  uv run python scripts/check_environment.py\n"
    )
    return False


def check_packages() -> bool:
    print("2. Packages")
    import importlib

    all_present = True
    for module_name, minimum in REQUIRED:
        try:
            module = importlib.import_module(module_name)
        except ImportError:
            print(f"   MISSING  {module_name}  (need >= {minimum})")
            all_present = False
            continue
        version = getattr(module, "__version__", "unknown")
        print(f"   ok       {module_name:<12} {version}")
    print()
    return all_present


def check_data(repo: Path) -> bool:
    print("3. Data files")
    data = repo / "data"
    all_present = True
    for name in EXPECTED_DATA_FILES:
        path = data / name
        if path.exists():
            print(f"   ok       {name:<22} {path.stat().st_size / 1024:8.1f} KB")
        else:
            print(f"   MISSING  {name}")
            all_present = False
    print()
    return all_present


def check_can_load(repo: Path) -> bool:
    print("4. Loading and computing")
    try:
        import pandas as pd

        prices = pd.read_csv(repo / "data" / "sp500_prices.csv", parse_dates=["date"])
        returns = prices.groupby("ticker")["close"].pct_change()
        print(f"   ok       {len(prices):,} price rows loaded")
        print(f"   ok       mean daily return {returns.mean():.6f}")
        print()
        return True
    except Exception as exc:  # noqa: BLE001 - we want to report anything at all
        print(f"   FAILED   {type(exc).__name__}: {exc}\n")
        return False


def main() -> int:
    repo = find_repo_root()
    print(f"Repository: {repo}\n")

    results = [
        check_interpreter(),
        check_packages(),
        check_data(repo),
        check_can_load(repo),
    ]

    if all(results):
        print("All checks passed. Open notebooks/00_environment_check.ipynb next.")
        return 0

    print("Some checks failed. See the Troubleshooting section of SETUP.md.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
