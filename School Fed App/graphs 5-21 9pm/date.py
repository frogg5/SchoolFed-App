import matplotlib.pyplot as plt
import pandas as pd
import csv

plt.style.use('fivethirtyeight')

col_list = ["dateandtime", "totalpriceusd"]

csv_data = pd.read_csv("docs/data.csv", usecols=col_list)


print(csv_data["dateandtime"])
print(csv_data["totalpriceusd"])

xlist = csv_data["dateandtime"].tolist()
head, sep, tail = xlist.partition('-2')
xlist.replace("-01", " January")
xlist.replace("-02", " February")
xlist.replace("-03", " March")
xlist.replace("-04", " April")
xlist.replace("-05", " May")
xlist.replace("-06", " June")
xlist.replace("-07", " July")
xlist.replace("-08", " August")
xlist.replace("-09", " September")
xlist.replace("-10", " October")
xlist.replace("-11", " November")
xlist.replace("-12", " December")

ylist = csv_data["totalpriceusd"].tolist()

with open('date.csv') as csvfile:
    riter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['date', 'totalpriceusd'])
    for i in range(len(xlist, ylist)):
    	writer.writerow(i)

col_list = ["date", "totalpriceusd"]

df = pd.read_csv("date.csv", usecols=col_list)

x = df["date"]
y = df["totalpriceusd"]


plt.xlabel('Date')
plt.ylabel('Total Spent ($)')
plt.bar(x, y)

plt.show()
