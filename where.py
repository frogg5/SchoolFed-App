import matplotlib.pyplot as plt
import pandas as pd
import csv

#graph for where you bought everything

def run():
    plt.style.use('fivethirtyeight')
    col_list = ["where", "totalpriceusd"]
    df = pd.read_csv("docs/data.csv", usecols=col_list)
    print(df["where"])
    print(df["totalpriceusd"])
    x = df["where"]
    y = df["totalpriceusd"]
    plt.xlabel('Location')
    plt.ylabel('Total Spent ($)')
    plt.bar(x, y)
    plt.show()
