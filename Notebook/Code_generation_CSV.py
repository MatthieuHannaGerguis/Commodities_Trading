import yfinance as yf
import pandas as pd

tickers = [
    'BZ=F', 'CL=F', 'RB=F', 'HO=F',     # Commodity futures (Brent, WTI, Gasoline, Heating Oil)
    'XLE', 'USO', 'XOP',                   # ETFs
    'BP', 'SHEL', 'TTE', 'E', 'EQNR',     # G10 equities
    'REPYY', 'WDS', 'PBR', 'CVX', 'XOM'   # G10 equities (continued)
]

data = yf.download(tickers, start='2019-01-01', end='2026-03-28', auto_adjust=True)
prices = data['Close']
prices = prices.rename(columns={'E': 'ENI'})
prices = prices[sorted(prices.columns)]
prices.to_csv('brent_energy_dataset.csv')

print(f"Done: {prices.shape[0]} rows x {prices.shape[1]} columns")
print(f"Tickers: {list(prices.columns)}")
print(f"\nMissing values:\n{prices.isnull().sum()}")