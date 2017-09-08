#changable label example
from tkinter import *

#hold onto global reference for root window
root = None
root_Two = None
#changable text inside Label
myText = None
myText_Two = None
#warning_One = None
count = 0 # Click Counter

def buttonPushed():
    global myText
    global count
    count += 1
    myText.set("Stop clicking its been %d times!" %(count))
    if count == 10:
        myText.set("Stop that!")
    if count == 15:
        myText.set("What the hell man?")
    if count == 30:
        myText.set("Alright you asked for it...")
    if count == 5:
        root_Two =Tk()
        root_Two.title("Angry!")
        myText_Two.set("HELLO!?!")

def addTextLabel_Two(root_Two):
    global myText_Two
    myText_Two = StringVar()
    myText_Two.set("")
    myLabel = Label(root_Two, textvariable=myText_Two)
    myLabel.pack()




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
    addTextLabel_Two(root_Two)
    root.title("Window Name")
    root.mainloop() #Start the event loop

main()
#https://cs.gmu.edu/~dfleck/classes/cs112/spring08/slides/tkinter.pdf
