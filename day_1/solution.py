import pandas as pd
import numpy as np


df = pd.read_csv("data.txt")  # add header measurement to input data

df['difference'] = np.sign(df.measurement - df.measurement.shift(1))
df.loc[df['difference'] == 1, 'result'] = 'increased'
df['result'].dropna()  # prints lengths in command line


df['sum'] = df.measurement + df.measurement.shift(1) + df.measurement.shift(2)
df['sum_difference'] = np.sign(df['sum'] - df['sum'].shift(1))
df.loc[df['sum_difference'] == 1, 'sum_result'] = 'increased'
df['sum_result'].dropna()  # prints lengths in command line
