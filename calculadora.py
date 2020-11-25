import tkinter

# Variables and stuff
root = tkinter.Tk()
root.title("Calculadora")
root.resizable(0,0)

num1 = 0
num2 = 0
operation = "-"

# Window -----
windownumber = tkinter.StringVar()
text = tkinter.Entry(root, textvariable=windownumber)
text.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)
text.config(justify="right")

# Buttons Calls -----
def factorial(x):

    if x == 1:
        return x

    elif x < 0:
        return "Factorial error"

    else:
        return x * factorial(x - 1)

def ButtonClearCall():

    windownumber.set("")
    num1 = 0
    num2 = 0
    operation = ""

def ButtonEraseCall():

    erasedstr = ""
    erase = []

    if windownumber.get() != "":
        erase = list(windownumber.get())
        del erase[-1]

        for i in erase:
            erasedstr += i
        
        windownumber.set(erasedstr)

    else:
        pass

def ButtonNumberCall(a):

    if "error" in windownumber.get():
        windownumber.set("")
        windownumber.set(windownumber.get() + a)

    elif windownumber.get() == "0":
        pass

    else:
        windownumber.set(windownumber.get() + a)

def ButtonComaCall():

    if windownumber.get() == "":
        pass

    elif "." in windownumber.get():
        pass

    else:
        windownumber.set(windownumber.get() + ".")

def ButtonProblemCall(a):

    global operation, num1

    if a == "-":
        if windownumber.get() == "":
            windownumber.set("-")
        else:
            num1 = windownumber.get()
            operation = "-"
            windownumber.set("")
    else:
        num1 = windownumber.get()
        operation = a
        windownumber.set("")

def ButtonEqualCall():

    global operation, num1, num2

    num2 = windownumber.get()

    if num1 != "" and num2 != "":

        windownumber.set("")

        if operation == "/":
            try:
                windownumber.set(float(num1) / float(num2))

            except ZeroDivisionError:
                windownumber.set("Zero division error")

        elif operation == "*":
            windownumber.set(float(num1) * float(num2))

        elif operation == "-":
            windownumber.set(float(num1) - float(num2))

        elif operation == "+":
            windownumber.set(float(num1) + float(num2))

        elif operation == "l":
            for i in range(int(num1)):
                if int(num2) ** i == int(num1):
                    windownumber.set(i)
                    break

            else:
                windownumber.set("Log error")

        elif operation == "r":
            for i in range(int(num2)):
                if i ** int(num1) == int(num2):
                    windownumber.set(i)
                    break

            else:
                windownumber.set("Root error")

        elif operation == "s":
            try:
                windownumber.set(float(num1) ** float(num2))

            except:
                windownumber.set("Range error")

        elif operation == "!":
            windownumber.set(factorial(int(num2)))

        else:
            windownumber.set("Operation error")
    
    else:
        windownumber.set("Number definition error")


# Row 1 -----
buttonclear = tkinter.Button(root, text="C", command=ButtonClearCall)
buttonclear.grid(row=1, column=0, sticky="we", padx=5, pady=5)

buttonerase = tkinter.Button(root, text="⌫", command=ButtonEraseCall)
buttonerase.grid(row=1, column=1, columnspan=2, sticky="we", padx=5, pady=5)

buttonresult = tkinter.Button(root, text="=", command=ButtonEqualCall)
buttonresult.grid(row=1, column=3, columnspan=2, sticky="we", padx=5, pady=5)


# Row 2 -----
button7 = tkinter.Button(root, text="7", command=lambda:ButtonNumberCall("7"))
button7.grid(row=2, column=0, sticky="we", padx=5, pady=5)

button8 = tkinter.Button(root, text="8", command=lambda:ButtonNumberCall("8"))
button8.grid(row=2, column=1, sticky="we", padx=5, pady=5)

button9 = tkinter.Button(root, text="9", command=lambda:ButtonNumberCall("9"))
button9.grid(row=2, column=2, sticky="we", padx=5, pady=5)

buttondiv = tkinter.Button(root, text="÷", command=lambda:ButtonProblemCall("/"))
buttondiv.grid(row=2, column=3, sticky="we", padx=5, pady=5)

buttonlog = tkinter.Button(root, text="log", command=lambda:ButtonProblemCall("l"))
buttonlog.grid(row=2, column=4, sticky="we", padx=5, pady=5)


# Row 3 -----
button4 = tkinter.Button(root, text="4", command=lambda:ButtonNumberCall("4"))
button4.grid(row=3, column=0, sticky="we", padx=5, pady=5)

button5 = tkinter.Button(root, text="5", command=lambda:ButtonNumberCall("5"))
button5.grid(row=3, column=1, sticky="we", padx=5, pady=5)

button6 = tkinter.Button(root, text="6", command=lambda:ButtonNumberCall("6"))
button6.grid(row=3, column=2, sticky="we", padx=5, pady=5)

buttonmult = tkinter.Button(root, text="x", command=lambda:ButtonProblemCall("*"))
buttonmult.grid(row=3, column=3, sticky="we", padx=5, pady=5)

buttonroot = tkinter.Button(root, text="√", command=lambda:ButtonProblemCall("r"))
buttonroot.grid(row=3, column=4, sticky="we", padx=5, pady=5)


# Row 4 -----
button1 = tkinter.Button(root, text="1", command=lambda:ButtonNumberCall("1"))
button1.grid(row=4, column=0, sticky="we", padx=5, pady=5)

button2 = tkinter.Button(root, text="2", command=lambda:ButtonNumberCall("2"))
button2.grid(row=4, column=1, sticky="we", padx=5, pady=5)

button3 = tkinter.Button(root, text="3", command=lambda:ButtonNumberCall("3"))
button3.grid(row=4, column=2, sticky="we", padx=5, pady=5)

buttonminus = tkinter.Button(root, text="-", command=lambda:ButtonProblemCall("-"))
buttonminus.grid(row=4, column=3, sticky="we", padx=5, pady=5)

buttonsqr = tkinter.Button(root, text="^", command=lambda:ButtonProblemCall("s"))
buttonsqr.grid(row=4, column=4, sticky="we", padx=5, pady=5)


# Row 5 -----
button0 = tkinter.Button(root, text="0", command=lambda:ButtonNumberCall("0"))
button0.grid(row=5, column=0, columnspan=2, sticky="we", padx=5, pady=5)

buttoncoma = tkinter.Button(root, text=",", command=ButtonComaCall)
buttoncoma.grid(row=5, column=2, sticky="we", padx=5, pady=5)

buttonplus = tkinter.Button(root, text="+", command=lambda:ButtonProblemCall("+"))
buttonplus.grid(row=5, column=3, sticky="we", padx=5, pady=5)

button = tkinter.Button(root, text="!", command=lambda:ButtonProblemCall("!"))
button.grid(row=5, column=4, sticky="we", padx=5, pady=5)


# Loop -----
root.mainloop()

