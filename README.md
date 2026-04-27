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
