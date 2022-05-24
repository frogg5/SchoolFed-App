import cv2
import pytesseract
import csv
import numpy

from whatisthetotal import whatIsTheTotal
imagefilename = "capture.png"

def analyze():
    def importLibraries():
        import cv2
        import pytesseract
        import csv
        import numpy
    def findPytesseractpath():
        textfile = open("pytesseractpath.txt", "r")
        data = textfile.read()
        textfile.close()
        return data
    def recolor(image):
        image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        se=cv2.getStructuringElement(cv2.MORPH_RECT , (8,8))
        bg=cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
        out_gray=cv2.divide(image, bg, scale=255)
        out_binary=cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU )[1]
    def readImage(pytpath, mode, imagefilename):
        pytp = pytpath
        #print(pytp)
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" #Default installation for Windows 10, might need to change directory depending on installation

        img = cv2.imread(imagefilename)

        recolor(img) #currently unimplemented due to inconsistency in testing

        if mode == "normal":
            ReceiptContents = pytesseract.image_to_string(img)
            ReceiptContents = ReceiptContents.splitlines()
            #print (ReceiptContents)
            return ReceiptContents
        else:
            #integer mode
            ReceiptContents = pytesseract.image_to_string(img, config='digits')
            ReceiptContents = ReceiptContents.splitlines()
            return ReceiptContents
    def getRidOfExtra(contents):
        newlistofitems = []
        for content in contents:
            if "$" in content:
                content = content.lower().replace(" ", "")
                newlistofitems.append(content)
            else:
                print("")
        return newlistofitems
    def splitintoname(itemsandcostlist):
        itemlist = []
        for item in itemsandcostlist:
            indexofdollar = item.find('$')
            x = item[0:indexofdollar]
            itemlist.append(x)
        return itemlist
    def splitintocost(itemsandcostlist):
        costlist = []
        for item in itemsandcostlist:
            indexofdollar = item.find('$')
            lengthofstr = len(item)
            if item.find(",") != -1:
                print("e")
                pass
            else:
                if item[lengthofstr-1] == "f":
                    x = item[indexofdollar+1:lengthofstr-1]
                else:
                    x = item[indexofdollar+1:lengthofstr]
                x = float(x)
                costlist.append(x)
        return costlist
    def combinetodict(lsofname, lsofcost):
        res = {lsofname[i]: lsofcost[i] for i in range(len(lsofcost))}
        #print(res)
        return res
    def findTotal(list):
        totalstr = ""
        totalstrls = []
        for item in list:
            item = item.lower()
        for item in list:
            item = item.lower()
            item.find("total")
            if item.find("total") == -1:
                print("")
            else:
                totalstr = item
                totalstrls.append(item)
        z = len(totalstrls)
        for item in totalstrls:
            x = 0
            for i in range(10):

                a = item.find(str(x))
                x = x + 1
                if a != -1:
                    abc = item.find(str(x))
                    return(int(item[abc:len(item)]))
                else:
                    return(False)
    def getDateTime():
        from datetime import datetime

        now = datetime.now()

        dt_string = now.strftime("%d-%m-%Y_%H:%M")
        print("d-m-y h-m", dt_string)
        return (dt_string)
    def getMonth():
        import datetime
        datem = datetime.datetime.now()
        datem = datem.month
        if datem == 1:
            return "JAN"
        if datem == 2:
            return "FEB"
        if datem == 3:
            return "MAR"
        if datem == 4:
            return "APR"
        if datem == 5:
            return "MAY"
        if datem == 6:
            return "JUN"
        if datem == 7:
            return "JUL"
        if datem == 8:
            return "AUG"
        if datem == 9:
            return "SEP"
        if datem == 10:
            return "OCT"
        if datem == 11:
            return "NOV"
        if datem == 12:
            return "DEC"
    def getDay():
        import datetime
        datem = datetime.datetime.now()
        return datem.day
    def getYear():
        import datetime
        datem = datetime.datetime.now()
        return datem.year
    def writetoCSV(total,location):
        import csv
        docsdir = "docs/data.csv"
        writelist = []
        with open(docsdir, 'a', encoding='UTF8') as f:
            writer = csv.writer(f)
            dateandtime = getDateTime()
            writelist. append(dateandtime)
            writelist.append(location)
            writelist.append(total)
            writelist.append(getMonth())
            writelist.append(getDay())
            writelist.append(getYear())
            writer.writerow(writelist)

        print("WROTE2CSV")
    def writetoCSVdict(dict, state):
        import csv
        docsdir = "docs/temporarydata.csv"
        writelist = []
        with open(docsdir, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            if state == True:
                dateandtime = getDateTime()
                writelist. append(dateandtime)
                writelist.append(dict)
                writer.writerow(writelist)
            else:
                writer.writerow(writelist)
    def wherepyGraph(): #lindens code
        import matplotlib.pyplot as plt
        import pandas as pd
        import csv

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
    def sortPyGraph(): #lindens code
        import pandas as pandasForSortingCSV
        import csv
        csv_data = pandasForSortingCSV.read_csv("docs/data.csv")
        csv_data.sort_values(csv_data.columns[2], axis=0, inplace=True)
        print(csv_data)
        x = csv_data["where"].tolist()
        y = csv_data["totalpriceusd"].tolist()
        print(x)
        print(y)
        #spent total at location
    def findTotalFromUser():
        total = whatIsTheTotal()
        return total
    def main():
        importLibraries()
        pytesseractpath = findPytesseractpath()
        print ("pytesseract path: " + pytesseractpath)

        readimagestring = readImage(pytesseractpath, "normal", imagefilename)
            #print(readimagestring)
        itemsandcostlist = getRidOfExtra(readimagestring)
            #print(itemsandcostlist)
        k_total = 0

        k_dictionarynameandcost = []

        if itemsandcostlist == []: #if $ symbol method did not work
            imgRecgnitionStatus = False
            print("imgRecognitionStatus", imgRecgnitionStatus)
            readimagestring = readImage(pytesseractpath, "normal", imagefilename)
            print(readimagestring)
            k_location = readimagestring[0]
            if findTotal(readimagestring) == False:
                totalUnknown = True
                print("Total unknown")
            else:
                k_total = findTotal(readimagestring)
                totalUnknown = False
        else: #if $ symbol method was successful
            imgRecgnitionStatus = True
            print("imgRecognitionStatus", imgRecgnitionStatus)
            k_location = readimagestring[0]
            lsofname = splitintoname(itemsandcostlist)
            lsofcost = splitintocost(itemsandcostlist)
            k_dictionarynameandcost = combinetodict(lsofname, lsofcost)
            print(k_dictionarynameandcost)
            k_total = k_dictionarynameandcost.get("total")
            print(k_total)
            if k_total == None:
                print("total unknown")
                totalUnknown = True
            else:
                totalUnknown = False


        if imgRecgnitionStatus == True:
            pass
        if imgRecgnitionStatus == False:
            pass

        if totalUnknown == True: #if we dont know what the total is
            print("find total")
            k_total = findTotalFromUser()
            writetoCSV(k_total,k_location)
            writetoCSVdict(k_dictionarynameandcost, False)
        else:
            writetoCSV(k_total,k_location) #writes and adds to data csv
            writetoCSVdict(k_dictionarynameandcost, True) #writes to temporary csv, overriden every run

        return(totalUnknown)
    main()
    #wherepyGraph()
    #sortPyGraph()
