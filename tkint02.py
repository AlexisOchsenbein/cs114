from tkinter import *

root = None

myText = None
count = 0



def buttonHello():
    global myText
    global count
    count += 1
    myText.set("Hello, for the %d time!" %(count))


def windowTitle(root):
    global myText
    myText = StringVar()
    myText.set("")
    myLabel = Label(root, textvariable=myText)
    myLabel.pack()




def main():
    global root
    root =Tk()
    myHello = Button(root,text="Show Text", command=buttonHello)
    myHello.pack()
    windowTitle(root)
    root.mainloop()
main()
