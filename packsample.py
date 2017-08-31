#pack_sample.py
from tkinter import *

#hole global root window reference
root = None
count = 0

def addButton(root,sideToPack):
    global count
    name = "Button" + str(count) + ""+sideToPack
    button = Button(root,text=name)
    button.pack(side=sideToPack)
    count +=1

def main():
    global root
    root = Tk() #where all widgets go
    #for i in range(5):
    addButton(root, TOP)
    addButton(root, LEFT)
    addButton(root, BOTTOM)
    root.mainloop() #start event loop

main()
