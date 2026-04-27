import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

stocks = ['AAPL', 'NVDA', 'RELIANCE.NS', 'BTC-USD', 'ETH-USD']

# download
data = yf.download(stocks, start='2020-01-01', end='2025-01-01')

price = data['Close'].dropna()

# returns
returns = price.pct_change().dropna()

# momentum (IMPORTANT FIX: no .mean())
mom12 = price.pct_change(252)
mom1 = price.pct_change(21)

signal = mom12 - mom1

# shift to avoid lookahead bias
signal = signal.shift(1).dropna()

# ranking (cross-sectional)
ranks = signal.rank(axis=1, ascending=False)

# longs & shorts
longs = ranks <= 2
shorts = ranks > (len(stocks) - 2)

# weights
weights = (longs.astype(int) - shorts.astype(int))
weights = weights.div(weights.abs().sum(axis=1), axis=0)

# align with returns
weights = weights.reindex(returns.index).ffill()

# strategy returns (before cost)
gross_returns = (weights * returns).sum(axis=1)

# turnover (how much position changes)
turnover = weights.diff().abs().sum(axis=1)

# transaction cost assumption
cost_per_trade = 0.001  # 0.1%

transaction_cost = turnover * cost_per_trade

# final strategy returns AFTER cost
strategy_returns = gross_returns - transaction_cost

# equity curve
equity_curve = (1 + strategy_returns).cumprod()

# plot
plt.figure(figsize=(10,5))
plt.plot(equity_curve)
plt.title("Equity Curve")
plt.show()

# Sharpe Ratio
sharpe = np.sqrt(252) * strategy_returns.mean() / strategy_returns.std()

# Drawdown
cum_max = equity_curve.cummax()
drawdown = (equity_curve - cum_max) / cum_max

max_drawdown = drawdown.min()

print("Sharpe Ratio:", sharpe)
print("Max Drawdown:", max_drawdown)

plt.figure(figsize=(10,5))
plt.plot(drawdown, color='red')
plt.title("Drawdown")
plt.show()