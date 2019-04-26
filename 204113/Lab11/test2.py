import pandas as pd
from math import log2

df = pd.read_csv("data1.txt")

df = df.drop("Film",axis=1)
column = df.columns
suc = df[column[3]]

a = df.drop(["USA","Europe"])
print(a)