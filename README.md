# Commodity Trading Games - Energy Sector (Brent Crude Oil)

### ESILV · Master Financial Engineering · Commodities Markets and Models · Spring 2026

**Professor**: J. Chevallier | **TD Leader**: W. Lebeda

**Authors**: Sacha KEREDAN & Matthieu HANNA GERGUIS (IF3)

---

## Overview

This repository contains our final project for the Commodities Markets and Models course. We designed and backtested two quantitative trading strategies on the energy commodity sector, with Brent Crude Oil (ICE Futures) as our primary anchor.

**Game #1 - Optimal Market-Neutral Trading** (Sacha KEREDAN)
Constructs a zero-beta portfolio of 5 energy assets using bi-objective optimization. Adapted from [Yang & Malik (2024)](https://doi.org/10.3390/ijfs12030077). The portfolio is completely insulated from oil price direction: realized beta = -0.039, R2 = 1.7% vs Brent.

**Game #2 - Beating Passive Strategies** (Matthieu HANNA GERGUIS)
Trades the Brent-Gasoline crack spread with dynamic risk management: volatility filter, trailing stop-loss, lookback optimization. Adapted from [Palazzi (2025)](https://doi.org/10.1002/fut.70018). Achieves a Calmar ratio of 0.982 with max drawdown of only -10.19%.

Both strategies are profitable in bull and bear regimes, while buy-and-hold Brent loses -26.12% in bear markets.

---

## Key Results (Out-of-Sample, January 2024 to March 2026)

| Metric | Game #1 (OTT) | Game #2 (Palazzi) | Buy & Hold Brent |
|---|---|---|---|
| Ann. Return | 6.01% | 10.00% | 20.00% |
| Ann. Volatility | 9.59% | 17.78% | 32.68% |
| Sharpe Ratio | **0.627** | 0.563 | 0.612 |
| Max Drawdown | -17.03% | **-10.19%** | -35.37% |
| Calmar Ratio | 0.353 | **0.982** | 0.565 |
| Brent Beta | -0.039 | partial | 1.000 |
| Bull Return | +7.41% | +15.81% | +38.91% |
| Bear Return | +4.12% | +18.19% | **-26.12%** |

---

## Dataset

17 energy assets, daily adjusted close prices from January 2019 to March 2026 (1,822 trading days), sourced from Yahoo Finance via `yfinance`.

| Category | Assets |
|---|---|
| Anchor | BZ=F (Brent Crude Oil Futures) |
| Commodity Futures | CL=F (WTI), RB=F (Gasoline), HO=F (Heating Oil) |
| Sector ETFs | XLE, USO, XOP |
| Equities (G10) | BP, SHEL, TTE, ENI, EQNR, REP, WDS, PBR, CVX, XOM |

The cointegration analysis found that only the crack spread (Brent vs Gasoline, p = 0.0034) is statistically significant at 5%. This relationship drives both strategies.

---

## Repository Structure

```
.
├── README.md
├── Data/
│   ├── brent_energy_dataset.csv                # Pre-built dataset (17 assets, 1822 days)
│   └── download_data.py                        # Script to regenerate the CSV (run locally)
├── Notebook/
│   ├── Game1.ipynb                             # Game #1 notebook (Colab-ready)
│   └── Game2.ipynb                             # Game #2 notebook (Colab-ready)
├── Report/
│   └── Report_KEREDAN_HANNA_GERGUIS.pdf        # Final report (18 pages)
└── Subject/
    ├── Books/                                   # Reference textbooks (Geman, Huisman)
    ├── Slides/                                  # Lecture slides (Lectures 1-4)
    └── Tds/                                     # Tutorial exercises (TD1-TD5)
```

---

## How to Run

Both notebooks run in Google Colab without any modification.

**Step 1.** Open the notebook in [Google Colab](https://colab.research.google.com/)

**Step 2.** Run the first two cells (install packages + imports)

**Step 3.** When prompted, upload `Data/brent_energy_dataset.csv`

**Step 4.** Run all cells: **Runtime > Run all**

No path to change, no API key needed, no parameter to tweak.

---

## Methodology

### Game #1 - Market-Neutral (Yang & Malik 2024)

Selects 5 assets cointegrated with Brent and optimizes portfolio weights to achieve zero market exposure. The optimization maximizes expected return minus a risk penalty, subject to a market-neutrality constraint (sum of beta-weighted positions = 0) and a no-leverage constraint (total allocation <= 100%).

Optimal weights: long RB=F (+24.6%), short HO=F (-49.1%), long XOP (+26.3%). Beta sum = 0.000.

Solved with `scipy.optimize.minimize` (SLSQP), equivalent to Gurobi for this convex problem.

### Game #2 - Pairs Trading (Palazzi 2025)

Trades the Brent-Gasoline crack spread (cointegration p = 0.0034, R2 = 94.1%, half-life = 19.2 days) with four risk management layers:

1. **Lookback optimization**: grid search over 30-252 days, optimal = 252 days, threshold = 0.7
2. **Volatility filter**: blocks entries when 30-day vol exceeds 1.5x average (blocks 6.2% of days)
3. **Trailing stop-loss**: exits when PnL drops 2.5% from peak
4. **Minimum holding period**: 5 trading days before any exit

---

## Course Connections

| Course Element | Application in Project |
|---|---|
| Lecture 1 (Spot Prices) | Stylized facts: fat tails (kurtosis 14.1), volatility clustering |
| Lecture 2 (Forward Curves) | Contango drag on USO, convenience yield |
| Lecture 3 (Correlations) | Engle-Granger cointegration, crack spread (Slide 36), DCC |
| Lecture 4 (Applications) | Crack spread as real option |
| TD2 (GARCH) | Volatility filter justification (persistence 0.988) |
| TD3 (Kalman) | Suggested improvement for time-varying betas and hedge ratios |
| TD4 (Schwartz-Smith) | Half-life estimation (19.2 days for crack spread) |
| TD5 (Regime-Switching) | Bull/bear regime analysis (Huisman & Mahieu 2003) |
| Geman (2005) | Brent market structure, commodity correlations |

---

## References

- Palazzi, R. B. (2025). Trading Games: Beating Passive Strategies in the Bullish Crypto Market. *Journal of Futures Markets*, 45(11). [GitHub](https://github.com/rafaelpalazzi/trading-games-crypto)
- Yang, H., & Malik, A. (2024). Optimal Market-Neutral Multivariate Pair Trading on the Cryptocurrency Platform. *Int. J. Financial Studies*, 12(3). [GitHub](https://github.com/Hongshen-Yang/optimal-trading-technique)
- Geman, H. (2005). *Commodities and Commodity Derivatives*. Wiley.
- Huisman, R. (2009). *An Introduction to Models for the Energy Markets*. Risk Books.
- Huisman, R., & Mahieu, R. (2003). Regime jumps in electricity prices. *Energy Economics*, 25(5).
- Engle, R. F. (2002). Dynamic Conditional Correlation. *J. Business & Economic Statistics*.

---

*Submitted on DVL - March 31, 2026*
