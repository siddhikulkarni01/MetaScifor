import tkinter as tk
from tkinter import *

m = Tk()

Label(m,text="firstname").grid(row=0)
Label(m,text="lastname").grid(row=1)
e1 = Entry(m)
e2 = Entry(m)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
m.title("siddhi")
button = Button(m,text="Stop",width=25,command=m.destroy)
button.grid(row=2, columnspan=2)

mainloop()