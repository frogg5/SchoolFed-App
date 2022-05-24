def whatIsTheTotal():
    def unkownTotalInput():
        import tkinter as tk

        frame = tk.Tk()
        frame.title("Enter $ in USD")
        frame.geometry('300x130')

        def printInput():
            inp = inputtxt.get(1.0, "end-1c")
            print(inp)
            import csv
            f = open('whatisthevalue.csv', 'w')
            writer = csv.writer(f)
            aaa = []
            aaa.append(float(inp))
            writer.writerow(aaa)
            f.close()
            frame.destroy()
            #print(inp)
            return(inp)

        inputtxt = tk.Text(frame,
                           height = 5,
                           width = 20)

        inputtxt.pack()

        printButton = tk.Button(frame,
                                text = "Confirm",
                                command = printInput)
        print(printButton)
        printButton.pack()

        lbl = tk.Label(frame, text = "")
        lbl.pack()
        frame.mainloop()

    def findUnknownValue():
        with open('whatisthevalue.csv') as f:
            lines = f.readlines()
            lines = float(lines[0])
        return(lines)

    unkownTotalInput()
    return findUnknownValue()
