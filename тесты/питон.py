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
counter = 0
b1 = Libraries("Florida", "fdsfadf", "fafaf")
b2 = Libraries("Floasdda", "fasddf", "fsdf")
b1.ff()
b2.ff()
b1.ff()
b2.ff()



