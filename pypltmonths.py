def plotGraphTotalSpentPerMonth(e):
    import matplotlib.pyplot as plt
    import pandas as pd
    from csv import reader

    '''with open('docs/data.csv', 'r') as readobj:
        csvreader = reader(readobj)
        for row in csvreader:
            currentMonth = row[3]'''


    data = pd.read_csv('docs/data.csv')

    df = pd.DataFrame(data)

    X = list(df.iloc[:, 3])
    Y = list(df.iloc[:, 2])

    month = df["month"].tolist()
    value = df["totalpriceusd"].tolist()

    filter = []
    filterv = []

    for i in range(len(month)):
        temp = month[i]
        if temp not in filter: #if month has not been recorded
            filter.append(month[i])
            filterv.append(value[i])
        else: # if month is already a row
            index = filter.index(month[i]) #find index of previous month
            print(index)
            print(value)
            filterv[index] = filterv[index] + value[i] #add on to previous month spending

    print(filter)
    print(filterv)

    newls = []
    newlsv = []
    for filt in filter:
        newls.append(str(filt))

    for filt in filterv:
        newlsv.append(int(filt))
    filter = ["a", "b", "c" , "d"]
    filterv = [1, 2, 3 , 4]

    # Plot the data using bar() method
    plt.bar(newls, newlsv, color='g')
    plt.title("")
    plt.xlabel("Month")
    plt.ylabel("Total Amount Spent")

    # Show the plot
    plt.show()
    #plt.savefig("totalbymonth.jpg")
