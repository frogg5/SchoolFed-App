import pandas as pandasForSortingCSV
import csv
import shutil

def writeImage():
    import shutil
    shutil.copy("images/Background.png", "images/bg.png")

def start():
    csv_data = pandasForSortingCSV.read_csv("docs/data.csv")
    csv_data.sort_values(csv_data.columns[2], axis=0, inplace=True)


    print(csv_data)

    x = csv_data["where"].tolist()

    y = csv_data["totalpriceusd"].tolist()

    temp = 0.0
    for item in y:
        temp+=item

    #print(x)
    #print(y)
    dictSorted = dict(zip(x,y))
    print("sum:", temp)
    print(x)
    print(y)
    return x,y, temp
    writeImage()


    #spent total at location
