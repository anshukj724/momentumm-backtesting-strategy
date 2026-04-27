
# 📊 Cross-Asset Momentum Strategy Backtest

## 🚀 Strategy Overview

This project implements a **cross-sectional momentum strategy** across equities and crypto assets.

The strategy:
- Computes 12-month and 1-month momentum
- Builds signal: `12M momentum − 1M momentum`
- Ranks assets daily
- Goes long top 2 and short bottom 2 assets
- Includes transaction cost modeling (0.1%)
- Evaluates performance using Sharpe Ratio and Drawdown


--

<img width="847" height="449" alt="download" src="https://github.com/user-attachments/assets/88f95de6-01f4-4aae-80a2-87c1aaed48b2" />



Sharpe Ratio: 0.6539635130623694
Max Drawdown: -0.3869016614697232



<img width="826" height="449" alt="download" src="https://github.com/user-attachments/assets/61a3dce7-23c8-4499-a206-c502e948cd7e" />
---

## 📈 Assets

- AAPL
- NVDA
- RELIANCE.NS
- BTC-USD
- ETH-USD

---

## ⚙️ Methodology

1. Data fetched via `yfinance` (2020–2025)
2. Returns and momentum signals computed
3. Cross-sectional ranking applied daily
4. Long/short portfolio constructed
5. Transaction costs applied based on turnover
6. Equity curve and risk metrics generated

---

## 📊 Performance Metrics

- Sharpe Ratio (annualized)
- Maximum Drawdown
- Equity Curve

---

## 🧮 Key Formula
