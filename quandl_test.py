import quandl
import pandas as pd


df = quandl.get("WIKI/GOOGL")
df["Adj. Half Open"] = df["Adj. Open"] / 2
df = df[["Adj. Open", "Adj. High", "Adj. Low", "Adj. Close", "Adj. Half Open"]]
print df.head()
