#https://www.youtube.com/watch?v=-tbWoZSi3LU

from tkinter import *
from tkinter import ttk

root = Tk()

root.title("Hello")

ttk.Button(root, text="This thing is working.").grid()

root.mainloop()



root = Tk()

root.title("Thingy")

frame = Frame(root)

labelText = StringVar()
label = Label(frame, textvariable=labelText)
button = Button(frame, text="Click Me")

labelText.set("This label works.")

label.pack()
button.pack()
frame.pack()



root.mainloop()

root = Tk()

root.title("Choose A Thing")

Label(root, text="Description").grid(row=0, column=0, sticky=W)
Entry(root, width=50).grid(row=0, column=1)
Button(root, text="submit").grid(row=0, column=8)

Label(root, text="Quality").grid(row=1, column=0, sticky=W)
Radiobutton(root, text="New", value=1).grid(row=2, column=0, sticky=W)
Radiobutton(root, text="Good", value=1).grid(row=3, column=0, sticky=W)
Radiobutton(root, text="Poor", value=1).grid(row=4, column=0, sticky=W)
Radiobutton(root, text="Damged", value=1).grid(row=5, column=0, sticky=W)

Label(root, text="Benefits").grid(row=1, column=1, sticky=W)
Checkbutton(root, text="Free Shipping").grid(row=2, column=1, sticky=W)
Checkbutton(root, text="Bonus Gift").grid(row=3, column=1, sticky=W)

root.mainloop()
