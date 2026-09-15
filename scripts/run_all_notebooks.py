"""Execute every notebook top to bottom and report failures.

    uv run python scripts/run_all_notebooks.py

Intended for the instructor: run this after editing a notebook, or at the start
of a semester after packages have been updated, to confirm the whole lab still
executes. Outputs are written to a scratch folder and discarded, so the
notebooks in the repository stay clean.

Exits non-zero if any notebook fails, so it can be wired into CI.
"""

from __future__ import annotations

import sys
import tempfile
import time
from pathlib import Path

ORDER = [
    "00_environment_check.ipynb",
    "01_pandas_fundamentals.ipynb",
    "02_returns_and_risk.ipynb",
    "03_features_and_targets.ipynb",
    "04_ml_credit_risk.ipynb",
    "05_ml_market_prediction.ipynb",
]


def find_repo_root() -> Path:
    here = Path(__file__).resolve()
    for candidate in [here.parent, *here.parents]:
        if (candidate / "notebooks").is_dir():
            return candidate
    raise SystemExit("Could not find the repository root.")


def main() -> int:
    import nbformat
    from nbclient import NotebookClient
    from nbclient.exceptions import CellExecutionError

    repo = find_repo_root()
    failures = []

    with tempfile.TemporaryDirectory() as scratch:
        for name in ORDER:
            path = repo / "notebooks" / name
            if not path.exists():
                print(f"SKIP   {name} (not found)")
                continue

            print(f"RUN    {name} ...", end=" ", flush=True)
            started = time.perf_counter()
            notebook = nbformat.read(path, as_version=4)
            client = NotebookClient(
                notebook,
                timeout=900,
                kernel_name="python3",
                resources={"metadata": {"path": str(repo)}},
            )
            try:
                client.execute()
            except CellExecutionError as exc:
                elapsed = time.perf_counter() - started
                print(f"FAILED in {elapsed:.1f}s")
                failures.append((name, str(exc).strip().splitlines()[-1]))
                continue

            elapsed = time.perf_counter() - started
            print(f"ok ({elapsed:.1f}s)")
            nbformat.write(notebook, Path(scratch) / name)

    print()
    if failures:
        print(f"{len(failures)} notebook(s) failed:\n")
        for name, message in failures:
            print(f"  {name}\n      {message}\n")
        return 1

    print("All notebooks executed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
