# Crosswalk — Duran Chapter 6 to the lab notebooks

**Randall E. Duran, *Financial Services Technology: Processes, Architecture,
and Solutions*, 3rd edition — Chapter 6, "Data Analytics"**

The chapter is organised around the idea that analytics in financial services
is mostly a data management problem, with the modelling as a comparatively
small final step. The lab is built to make students feel that proportion:
three notebooks of data work before any model is fitted.

> **A note on section numbers.** This crosswalk maps to the chapter's *themes*
> rather than to numbered sections, because the themes are stable across
> printings. Add your edition's section numbers in the blank column when you
> teach it.

---

## Theme-by-theme mapping

| § | Chapter theme | Where it lands | What students actually do |
|---|---|---|---|
| | **The analytics maturity ladder** — descriptive, diagnostic, predictive, prescriptive | NB 02 → 03 → 04/05 | The notebook sequence *is* the ladder. NB 02 is descriptive; NB 03 builds predictive inputs; NB 04/05 are predictive; the profit-based cut-off at the end of NB 04 is prescriptive. |
| | **Data as raw material; data quality** | NB 01 §1–2, §9 | Parse dates on load; `describe()` as a data-quality screen; distinguishing market holidays from missing observations; forward fill versus interpolation. |
| | **Data integration, reference data, the security master** | NB 01 §8 | Joining prices to a GICS security master; inner versus left join; a deliberately damaged master to show how an inner join silently drops positions from a risk report. |
| | **Structured vs unstructured; storage formats** | NB 01 §6–7 | Long versus wide representation and why market data is transmitted one way and analysed the other; `resample` for reporting periods. |
| | **ETL and the data pipeline** | NB 03 (whole notebook) | The notebook is an ETL pipeline: extract CSVs, transform into features with `groupby().transform()`, load a modelling table to `data/processed/`. |
| | **Data governance, lineage, reproducibility** | Repo design; NB 00 §2; NB 04 §3 | Pinned versions in `uv.lock`; recorded library versions; documented provenance in `data/README.md`; the fair-lending section as governance in practice. |
| | **Descriptive analytics and visualisation** | NB 02 (whole notebook) | Returns, annualisation, Sharpe, rolling volatility, drawdown, correlation, distribution and tail behaviour, beta. Includes an explicit passage on choosing a colour scale from the data. |
| | **Big data / velocity** | NB 01 §4 | Vectorised pandas operations versus row loops, and why the difference decides whether a report finishes. |
| | **Predictive analytics and machine learning** | NB 04, NB 05 | Logistic regression, decision tree, random forest, gradient boosting, ridge; classification and regression; cross-validation and walk-forward validation. |
| | **Model risk and validation** | NB 03 §3–4; NB 04 §7, §9; NB 05 §1 | Look-ahead bias demonstrated numerically; train/test discipline; overfitting shown as a train–test gap; base-rate and persistence baselines; standard errors on claimed improvements. |
| | **Credit risk analytics** | NB 04 | Full credit-scoring workflow on the Statlog German Credit data, ending in a profit-maximising approval cut-off. |
| | **Market risk analytics** | NB 02 §4, §7; NB 05 Task B | Realised versus implied volatility; historical, parametric and expected-shortfall VaR; forecasting next-month volatility. |
| | **Regulation, ethics, explainability** | NB 04 §3, §6, §8 | ECOA/Regulation B; proxy discrimination and disparate impact; why logistic regression survives in regulated lending; odds ratios as adverse-action reasons. |
| | **Analytics in practice — where it pays** | NB 05 §1–2 | The direct contrast between a task with no signal (direction) and one with a real, modest signal (volatility), and what distinguishes them. |

---

## If you are teaching to a fixed number of sessions

**Three 75-minute sessions**

| Session | Notebooks | Chapter themes covered |
|---|---|---|
| 1 | 00, 01 | Data as raw material, data quality, integration, storage formats |
| 2 | 02, 03 | Descriptive analytics, visualisation, ETL, model risk foundations |
| 3 | 04, 05 | Predictive analytics, credit and market risk, regulation, validation |

**Two 75-minute sessions** — set 00 and 01 as pre-work, then:

| Session | Notebooks |
|---|---|
| 1 | 02, 03 |
| 2 | 04, 05 (§10 of NB 04 is the highest-value 15 minutes in the lab) |

**One session as a demonstration** — run 02 §2–5 and 05 §1 live. Those two
blocks carry the descriptive-analytics material and the central honesty lesson;
everything else can be assigned.

---

## Where the lab deliberately goes beyond the chapter

Four additions worth flagging when you teach it, because students will ask why
they are there:

1. **Look-ahead bias as a numerical demonstration** (NB 03 §4). The chapter
   discusses model risk in general terms. The notebook builds a cheating
   feature, shows its correlation with tomorrow's return jump from ~0.01 to
   ~0.63, and then deletes it. Students remember the number.

2. **Fair lending in depth** (NB 04 §3). Proxy discrimination and disparate
   impact are given as much space as the modelling. For finance majors heading
   into lending, credit analysis, or bank technology, this is the section most
   likely to matter in their first job.

3. **A negative result presented as a result** (NB 05 Task A). Direction
   prediction is run properly and fails, and the notebook treats saying so as
   the professional outcome. This is the main inoculation against the
   fintech-course failure mode where students leave believing a random forest
   beats the market.

4. **Threshold selection from expected profit** (NB 04 §10), with the
   closed-form optimum $M/(M+L)$ derived and then checked numerically — and the
   discrepancy between formula and grid used to teach calibration and sampling
   noise. This is the bridge from a model output to a business decision, which
   is where Duran's prescriptive tier actually lives.

---

## Assessment ideas tied to the chapter

| Assessment | Notebook | Chapter theme assessed |
|---|---|---|
| Complete the in-notebook exercises | All | Applied competence |
| Write a one-page data-quality memo on `sp500_prices.csv` | NB 01 | Data quality and governance |
| Reproduce the risk table for a different five-year window and explain what changed | NB 02 | Descriptive analytics, model stability |
| Identify three leakage risks in a supplied "student" notebook | NB 03 | Model risk and validation |
| Write a model card for the credit model: intended use, data, fair-lending testing, monitoring | NB 04 | Governance, regulation, explainability |
| Build a third prediction target with a named baseline, and report honestly | NB 05 | Predictive analytics and validation discipline |
