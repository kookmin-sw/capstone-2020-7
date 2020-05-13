import pandas as pd

temp = {}
for i in range(5):
    temp[i] = [each for each in range(100)]

df = pd.DataFrame(temp)
df.to_csv("./temp.csv", index=False)
