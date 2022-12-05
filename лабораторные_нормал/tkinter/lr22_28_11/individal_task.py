from tkinter import *
root = Tk() 
root.title("Проектная организация")
root.geometry("500x500+500+200")
root.minsize(200, 150)
root.maxsize(400, 300)


label = Label(text="Отделы")
label.pack()
label.place(x=10, y=10)


label1 = Label(text="Сотрудники")
label1.pack()
label1.place(x=150, y=10)

label2 = Label(text="Организации")
label2.pack()
label2.place(x=300, y=10)

label3 = Label(text="Договора")
label3.pack()
label3.place(x=70, y=150)

label4 = Label(text="Проектные работы")
label4.pack()
label4.place(x=200, y=150)

root.mainloop()