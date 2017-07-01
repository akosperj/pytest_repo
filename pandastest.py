import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

av = pd.read_csv("NASDAQ.MSFT.csv")
av = av.rename(columns={av.columns.values[0]: "date"})
av["date"]=pd.to_datetime(av["date"])
av=av.set_index("date")

yahoo = pd.read_csv("MSFT.csv")
yahoo = yahoo.rename(columns={yahoo.columns.values[0]: "date"})
yahoo["date"]=pd.to_datetime(yahoo["date"])
yahoo=yahoo.set_index("date")

close = pd.DataFrame(av["close"])

close = close.rename(columns={"close": "AV"})
close["yahoo"]=yahoo["Close"]
close.plot()
plt.show(block=True)
pass
