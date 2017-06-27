from bokeh.plotting import figure, output_file, show

import pandas as pd
import numpy as np
import csv

df = pd.read_csv("MSFT.csv")

print(df)


df.plot()

