from tkinter import *
from tkinter import ttk
from tkinter.messagebox import OK, INFO, showinfo

root = Tk()
root.title(" METANIT.COM ")
root.geometry("250x200")

def click():
    showinfo(title="METANIT.COM",
    message="Добро пожаловать на сайт METANIT.COM",
    detail="Hello World!", icon=INFO, default=OK)

ttk.Button(text="Click", command=click).pack(anchor="center", expand=1)

root.mainloop()