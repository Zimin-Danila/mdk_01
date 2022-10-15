# Создать класс с предметной областью библиотеки города
# Для того чтобы провести тест с подсчетом нужно ввести переменные книги в каждой библиотеке и количество библиотек
# После чего узнать общее количество книг
# 
import pickle
     
class Biblioteki_city(): #Создание библиотек с переменными: кол-во книг, номер библиотеки
    def __init__(self, book_in, nomer):
        self.book_in = book_in
        self.nomer = nomer

#Конструктор 
    def books(self): #  Вывод информации о количестве всех книгах из определенной библиотеки
        x =  b1.book_in + b2.book_in + b3.book_in + b4.book_in
        return (f"Вы находитесь в библиотеке под номером {self.nomer}. Сумарное количество книг во всех библиотеках города равно {x}")

    def books_test(self): # unittest
        x =  b1.book_in + b2.book_in + b3.book_in + b4.book_in
        return x

#Сериализация
    def serialize(self): # Сериализация номера библиотеки
        with open('C:\\Programming\\MDK\\MDK_01_01\\лабораторные_нормал\\lr2_12_10\\test_pickuli.pkl', 'wb') as f:
            pickle.dump(self.nomer, f)
        f.closed

#Десериализация
    def deserialize(self): #Десериализация номера библиотеки
        with open('C:\\Programming\\MDK\\MDK_01_01\\лабораторные_нормал\\lr2_12_10\\test_pickuli.pkl', 'rb') as f:
            biblioteki = pickle.load(f)
        f.closed
        return biblioteki

#Деструктор
    #def __del__(self): # Уничтожение экземпляра
        #print(f"На библиотеку {self.nomer} упал метеорит ☺")

                #Наследование
class Biblioteka(Biblioteki_city):
    def __init__(self,book_in,nomer, name, kolvo_otdelov):
        super().__init__(book_in, nomer)
        self.name = name
        self.kolvo_otdelov = kolvo_otdelov

    def Nazvanie(self):
        print(f"Название данной библиотеки {self.name}")

    def Otdelbi(self):
        x = (self.book_in // 500)+1
        print(f"Количество отделов данной библиотеки равно {x}")
        
    #Полиморфизм
    def books(self):
        print(f"Количество книг в этой библиотеке: {self.book_in} шт.")
b1 = Biblioteki_city(1000, 1)
b2 = Biblioteki_city(14999, 2)
b3 = Biblioteki_city(364, 3)
b4 = Biblioteki_city(8564, 4)
print(b1.books())
b2 = Biblioteka(b2.book_in, b2.nomer, "Florida", 1)
b2.Nazvanie()
b2.Otdelbi()
b2.books()




b1.serialize()
print(b1.deserialize())
b4.serialize()
print(b4.deserialize())
#del b1