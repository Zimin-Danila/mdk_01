from tkinter import *
from tkinter import ttk
root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

for c in range(2): root.columnconfigure(index=c, weight=1)
for r in range(2): root.rowconfigure(index=r, weight=1)

btn2 = ttk.Button(text="button 2")
btn2.grid(row=0, column=1, rowspan=2, ipadx=6, ipady=55, padx=5, pady=5)

btn1 = ttk.Button(text="button 1")
btn1.grid(row=0, column=0, ipadx=6, ipady=6, padx=5, pady=5)

btn3 = ttk.Button(text="button 3")
btn3.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)


root.mainloop()