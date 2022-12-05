from tkinter import *
from tkinter import ttk
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
btn = ttk.Button(text="Click me")
btn.place(relx=0.5, rely=0.5, anchor="c", width=80, height=40)
root.mainloop()