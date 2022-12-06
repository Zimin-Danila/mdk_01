from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
python_logo = PhotoImage(file="C:\Programming\mdk_01\лабораторные_нормал\\tkinter\lr14_06_12\python.png")
label = ttk.Label(image=python_logo)
label.pack()
root.mainloop()