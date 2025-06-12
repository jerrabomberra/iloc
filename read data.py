import pandas as pd


df = pd.read_csv("iloc\Data.csv")

print(df.iloc[1:3,0:4])

print(df.iloc[1,0:])


