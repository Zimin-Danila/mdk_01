import pickle
counter = 0
class Libraries(): #Класс "Библиотеки" с переменными: название, адрес,город.
    
    def __init__(self, name, adress, city):
        self.name = name
        self.adress = adress
        self.city = city
        
    
    def Name(my_func):
        
        def wrapper(self, *args, **kwargs):
            my_func(self, *args, **kwargs)
            global counter
            counter += 1
            print ('Название данной библиотеки', self.name)
            print(f'Количество запросов метода: {counter}')
        return wrapper
    @Name
    def ff(self):
        pass


class Reading_rooms(): #Класс "Читательные залы" с переменными: название читательного зала, 
                       #библиотека, количество единиц литературы, количество посадочных мест, 
                       #время работы, этаж, количество сотрудников.
    """Класс читательные залы с какими-либо объектами"""
    counter = 0
    def __init__(self, nameRr, lib, am_books, am_place, wk_time, floor, am_worker):
        
        self.__lib = lib
        self.am_books = am_books
        self._am_place = am_place
        self.wk_time = wk_time
        self.floor = floor 
        self.am_worker = am_worker
    


        
        if  isinstance(nameRr, str):
            self.nameRr = nameRr
        else:                                   
            raise InvalidNameError(nameRr)
    
    #Перегрузка операций
    def __add__(self, plac):
        self._am_place += plac
        
    def __call__(self, plac):
        self._am_place = plac

    def Pl(self):
        print(f"Количество мест:{self._am_place}")

    @property
    def libr(self):
        return self.__lib

    def books(self): #  Вывод информации о количестве всех книгах из определенной библиотеки
        x =  b1.am_books + b2.am_books + b3.am_books + b4.am_books
        return (f"Вы находитесь в библиотеке с названием <<{self.__lib}>>. Суммарное количество книг во всех библиотеках города равно {x}")

    def books_test(self): # unittest
        x =  b1.am_books + b2.am_books + b3.am_books + b4.am_books
        return x

    def Name(self):
        return f"<<{self.__lib}>>"

    def Bk(self):
        print(self.am_books)
    


        #Сериализация
    def serialize(self): # Сериализация номера библиотеки
        with open('C:\\Programming\\mdk_01\\лабораторные_нормал\\lr4_12_10\\test_pickuli.pkl', 'wb') as f:
            pickle.dump(self.wk_time, f)
        f.closed

#Десериализация
    def deserialize(self): #Десериализация номера библиотеки
        with open('C:\\Programming\\mdk_01\\лабораторные_нормал\\lr4_12_10\\test_pickuli.pkl', 'rb') as f:
            biblioteki = pickle.load(f)
        f.closed
        print(biblioteki)


    #def __del__(self): # Уничтожение экземпляра
            #print(f"На библиотеку <<{self.lib}>> упал метеорит ☺")
        




class Human():
    def __init__(self, surname = "Зимин", name="Данила", patronymic="Викторович", age="18"):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.age = age

    def Initials(self):
        return (self.surname[0]+self.name[0]+self.patronymic[0])


class Readers(): #Класс "Читатели" с переменными: фамилия, имя, отчество, возраст, 
                 #категория читателя, место работы или учебы, дата регистрации в библиотеке.
    def __init__(self, initil, surname = "Зимин", name="Данила", patronymic="Викторович", age="18", rd_ctg="Начинающий", dt_rg="01.08.2020"):
        self.reader = Human(surname, name, patronymic, age)#Ассоциация
        self.rd_ctg = rd_ctg
        self.dt_rg = dt_rg
        self.fio = initil # Агрегация
        
    def __str__(self):
        return f'Фамилия:{self.reader.surname}, Имя:{self.reader.name}, Отчество:{self.reader.patronymic},\
Возраст:{self.reader.age}, Категория читателя:{self.rd_ctg}, Дата регистрации:{self.dt_rg}'

    def Categori(self):
        return self.fio.Initials()

    def LevelUp(self, level):
        self.rd_ctg = level
        print(f'Вы повышены! Ваша категория - {self.rd_ctg}')
class Literature(): #Класс "Литература" с переменными: название, категория литературы, 
                    #автор, издательство, год издательства, количество страниц, читательный зал.
    def __init__(self, name, ctg_lt, author, publisher, yr_pub, am_page, read_room):
        self.name = name
        self.ctg_lt = ctg_lt
        self.author = author
        self.publisher = publisher
        self.yr_pub = yr_pub
        self.am_page = am_page
        self.read_room = read_room

class Lt_output(): #Класс "Выдача литературы" с переменными: читатель, литература, 
                   #дата выдачи, срок выдачи, вид выдачи, наличие залога.
    def __init__(self, reader, liter, dt_out, pd_out, type_out, collaterel=None):
        self.reader = reader
        self.liter = liter
        self.dt_out = dt_out
        self.pd_out = pd_out
        self.type_out = type_out
        self.collaterel = collaterel

class Book(Reading_rooms):
    def __init__(self, nameRr, lib, am_books, am_place, wk_time, floor, am_worker, am_page):
        super().__init__(nameRr, lib, am_books, am_place, wk_time, floor, am_worker)
        self.am_page = am_page


    #На одной странице 1000 символов
    def Symbols(self):
        print(f"В данной книге {self.am_page*1000} символов")

        
    #Полиморфизм
    def books(self):
        print(f"Количество книг в этом читальном зале: {self.am_books} шт.")

class InvalidNameError(Exception):
    def __init__(self, nameRra):
        self.nameRra = nameRra

    def __str__(self):
        return f"Неправильное название - {self.nameRra}! Название состоит из цифр, а должно из букв!"



#Экземпляры проекта
try:
    lib1 = Libraries("Florida", "fdsfadf", "fafaf")
    lib2 = Libraries("Floasdda", "fasddf", "fsdf")
    b1 = Reading_rooms("Пионерия", "Ленинская", 11589, 150, "8.00 - 19.00", 2, 20)
    b2 = Reading_rooms("Пролетариат", "Ленинская", 15860, 200, "8.00 - 21.00", 3, 34)
    b3 = Reading_rooms("Свобода", "Капитализм", 8469, 80, "6.00 - 18.00", 15, 15)
    b4 = Reading_rooms("Рынок", "Капитализм", 50214, 500, "10.00 - 22.00", 12, 51)
    b6 = Libraries("Ленин", "Колотушкина 1", "Мухово")
    h2 = Human()
    h1 = Readers(h2)
    #print(h1)
    #h1.LevelUp("Опытный")
    #print(h1)
    #print(h1.Categori())
    b1.Pl() #150
    b1(187) #187
    b1.Pl() #187
    b1 + 8 #195
    b1.Pl() #195
    #print(Reading_rooms.__doc__)

    #lib1.ff()
    #lib2.ff()
    #lib1.ff()
    #lib2.ff()


    
    #print(b2.Name())

    #b2 = Book(b2.nameRr, "Ленинская", b2.am_books, b2.am_place, b2.wk_time, b2.floor, b2.am_worker, 1054)
    #b2.Symbols()
    #b2.books()
    #Методы проекта
    #print(b1.Name())
    #print(b1.books())
    #del b1
    #b1.serialize()
    #b1.deserialize()
    #b2.serialize()
    #b2.deserialize()
except InvalidNameError as e:
    print(e)