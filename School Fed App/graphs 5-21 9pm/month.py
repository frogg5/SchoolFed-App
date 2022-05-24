import matplotlib.pyplot as plt
import pandas as pd
import csv

plt.style.use('fivethirtyeight')

col_list = ["dateandtime", "totalpriceusd"]

df = pd.read_csv("test.csv", usecols=col_list)


print(df["dateandtime"])
print(df["totalpriceusd"])





x = df["dateandtime"]
y = df["totalpriceusd"]


plt.xlabel('Month')
plt.ylabel('Total Spent ($)')
plt.bar(x, y)

plt.show()