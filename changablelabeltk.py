#changable label example
from tkinter import *

#hold onto global reference for root window
root = None

#changable text inside Label
myText = None
count = 0 # Click Counter

def buttonPushed():
    global myText
    global count
    count += 1
    myText.set("Stop clicking its been %d times!" %(count))


def addTextLabel(root):
    global myText
    myText = StringVar()
    myText.set("")
    myLabel = Label(root, textvariable=myText)
    myLabel.pack()

def main():
    global root
    root =Tk()  #creates the root (base) window where all widgets go
    myButton = Button(root,text="Show Text",command=buttonPushed)
    myButton.pack()
    addTextLabel(root)
    root.mainloop() #Start the event loop

main()
