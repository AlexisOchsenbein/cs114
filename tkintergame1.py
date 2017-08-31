from tkinter import *

root = None

entryBox = None

def buttonPushed():
    global entryBox #root
    #print("button pushed!")
    txt = entryBox.get()
    #root.destroy()

def createTextBox(parent):
    global entryBox
    entryBox = Entry(parent)
    entryBox.pack()

def main():
    global root
    root =Tk()
    #w = Label(root, text="Hello, world!")
    #w.pack()

    myButton = Button(root, text="exit",command=buttonPushed)
    myButton.pack()
    createTextBox(root)
    root.mainloop()

main()
