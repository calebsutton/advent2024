import pandas as pd
df = pd.read_csv('input.txt', engine="python", header=None, sep="   ")
results = df.apply(lambda x: len(df.loc[df[1] == x[0]]) * x[0], axis=1).sum()
print(results)