import pandas as pd
df = pd.read_csv('input.txt', engine="python", header=None, sep="   ")
df[0] = df[0].sort_values(ignore_index=True)
df[1] = df[1].sort_values(ignore_index=True)
results = df.apply(lambda x: abs(x[1] - x[0]), axis=1).sum()
print(results)