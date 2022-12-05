from tkinter import *
root = Tk() # создаем корневой объект - окно
root.title("Приложение на Tkinter")
root.geometry("300x250")
# устанавливаем размеры окна
# устанавливаем заголовок окна
label = Label(text="Hello METANIT.COM ") # создаем текстовую метку
label.pack()
# размещаем метку в окне
root.mainloop()