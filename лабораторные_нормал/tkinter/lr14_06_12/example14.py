from tkinter import *
from tkinter import ttk

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

def click():
    window = Tk()
    window.title("Новое окно")
    window.geometry("250x200")
    label = ttk.Label(window, text="Принципиально новое окно")
    label.pack(anchor=CENTER, expand=1)

button = ttk.Button(text="Создать окно", command=click)
button.pack(anchor=CENTER, expand=1)

root.mainloop()