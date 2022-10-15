class Car():
    """Класс по созданию автомобиля"""
    def __init__(self, make, model, year, pow_eng, nal_stavka, per_vlad, pov_koff, lgot):
        """Ициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.pow_eng = pow_eng
        self.nal_stavka = nal_stavka
        self.per_vlad = per_vlad
        self.pov_koff = pov_koff
        self.lgot = lgot

    
    def description_name(self):
        """Возращаем описание автомобиля"""
        desc = str(self.year) + ' ' + self.make + ' ' + self.model
        return desc.title()
    
    def read_odometer(self):
        """Выводим пробег авто"""
        print("Пробег этого авто " + str(self.odometer_reading) + "км")

    def update_odometer(self, km):
        """Устанавливаем значение на одометре"""
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("Не страдай фигней")

    def increment_odometer(self, km):
        """Увелечение показания одометра на заданную величину(Нужно придумать условие)"""
        if km >= 0: #Если пробег будет отрицательным, то программа выведет старый пробег, т.к. это невозможно
            self.odometer_reading += km
        else:
            print('Законы логики нарушаешь!')

    def rachet(self):
        """Метод по расчету транспортного налога"""
        podschet = self.pow_eng * self.nal_stavka *(self.per_vlad)* self.pov_koff - self.lgot
        print('Ваш транспортный налог составляет ' + str(int(podschet)) + ' рублей' + '.')


waitan = Car("Volkswagen", "Golf", 2004, 160.48, 45, 1, 1, 0)
print(waitan.description_name())
waitan.update_odometer(93000)
waitan.read_odometer()
waitan.rachet()
