from tkinter import *
from tkinter import ttk

root = Tk() 
root.title("METANIT.COM")
root.geometry("250x150")

btn = ttk.Button(text="Click")
btn.pack()

btn["text"]="Send"
btnText=btn["text"]
print(btnText)

root.mainloop()