from tkinter import *
from tkinter import ttk

root = Tk() 
root.title("METANIT.COM")
root.geometry("250x200")

btn = ttk.Button(text="Click me", state=["disabled"])
btn.pack()

root.mainloop()