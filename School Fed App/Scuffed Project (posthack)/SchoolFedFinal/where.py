import matplotlib.pyplot as plt

import pandas as pd

import csv

from matplotlib.pyplot import figure

def run():
    plt.style.use('fivethirtyeight')

    col_list = ["where", "totalpriceusd"]

    df = pd.read_csv("docs/data.csv", usecols=col_list)

    print(df["where"])

    print(df["totalpriceusd"])

    x = df["where"]

    y = df["totalpriceusd"]

    figure(num=None, figsize=(70, 50), dpi=80, facecolor='w', edgecolor='k')

    plt.xlabel('Location')

    plt.ylabel('Total Spent ($)')

    plt.bar(x, y)
    #plt.rc('axes', titlesize=100)
    plt.rc('xtick', labelsize=60)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=60)

    plt.savefig('saved_figure.png')
    
