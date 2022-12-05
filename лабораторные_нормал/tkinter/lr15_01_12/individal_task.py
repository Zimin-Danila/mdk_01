from tkinter import *
from tkinter import ttk

def clicking():
    content = btn0["text"]
    print(f"Кнопка <<{content}>> нажата")
def clicking1():
    content = btn1["text"]
    print(f"Кнопка <<{content}>> нажата")
def clicking2():
    content = btn2["text"]
    print(f"Кнопка <<{content}>> нажата")
def clicking3():
    content = btn3["text"]
    print(f"Кнопка<<{content}>> нажата")
def clicking4():
    content = btn4["text"]
    print(f"Кнопка <<{content}>> нажата")

    

root = Tk() 
root.title("Проектная организация")
root.geometry("500x300+500+200")
root.minsize(200, 150)
root.maxsize(600, 600)


label0 = Label(text="Отделы")
label0.place(x=70, y=10)

label1 = Label(text="Сотрудники")
label1.place(x=200, y=10)

label2 = Label(text="Организации")
label2.place(x=350, y=10)

label3 = Label(text="Договора")
label3.place(x=100, y=150)

label4 = Label(text="Проектные работы")
label4.place(x=300, y=150)

btn0 = ttk.Button(text="Информация об отделах", command=clicking)
btn0.place(x=15, y=50)

btn1 = ttk.Button(text="Информация о сотрудниках", command=clicking1)
btn1.place(x=155, y=100)

btn2 = ttk.Button(text="Информация об организациях", command=clicking2)
btn2.place(x=300, y=50)

btn3 = ttk.Button(text="Информация о договорах", command=clicking3)
btn3.place(x=50, y=200)

btn4 = ttk.Button(text="Информация о проектных работах", command=clicking4)
btn4.place(x=250, y=200)

root.mainloop()