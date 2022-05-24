def plotGraphTotalSpentPerDay():
    import matplotlib.pyplot as plt
    import pandas as pd
    from csv import reader
    from datetime import datetime

    currentDay = datetime.now().day
    currentMonth = datetime.now().month


    if currentMonth == 1:
        currentMonth = "JAN"
    elif currentMonth == 2:
        currentMonth = "FEB"
    elif currentMonth == 3:
        currentMonth = "MAR"
    elif currentMonth == 4:
        currentMonth = "APR"
    elif currentMonth == 5:
        currentMonth = "MAY"
    elif currentMonth == 6:
        currentMonth = "JUN"
    elif currentMonth == 7:
        currentMonth = "JUL"
    elif currentMonth == 8:
        currentMonth = "AUG"
    elif currentMonth == 9:
        currentMonth = "SEP"
    elif currentMonth == 10:
        currentMonth = "DEC"
    elif currentMonth == 11:
        currentMonth = "NOV"
    elif currentMonth == 12:
        currentMonth = "DEC"



    data = pd.read_csv('docs/data.csv')

    df = pd.DataFrame(data)

    month = df["month"].tolist()
    day = df["day"].tolist()
    value = df["totalpriceusd"].tolist()

    week = []
    filterv = []

    for i in range(currentDay-6, currentDay+1): #add all past 7 days
        week.append(i)
        filterv.append(0)

    print(week)


    for i in range(len(month)):
        if month[i] == currentMonth and day[i] in week: #if correct month and in 7 day range
            index = week.index(day[i])#find index of day
            filterv[index] = filterv[index] + value[i]#add value




    # Plot the data using bar() method
    plt.bar(week, filterv, color='g')
    plt.title("")
    temp = "Days of "+ str(currentMonth)
    plt.xlabel(temp)
    plt.ylabel("Total Amount Spent")

    # Show the plot
    plt.show()
    plt.savefig("totalbyday.jpg")
