from tkinter import *
from tkinter import ttk
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")
label = ttk.Label(text="Hello Tkinter", borderwidth=2, relief="ridge", padding=8)
label.pack(expand=True)
root.mainloop()