import string

# Алфавит
class Alphabet:

    def __init__(self, language, letters_str):
        self.lang = language
        self.letters = list(letters_str)

    # Печатаем все буквы алфавита
    def print(self):
        print(self.letters)

    # Возвращаем количество букв в алфавите
    def letters_num(self):
        len(self.letters)




   

# Английский алфавит
class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    # Проверяем, относится ли буква к английскому алфавиту
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return ("Буква " + letter + " находится в данном алфавите")
        return ("Буква " + letter + " не находится в данном алфавите")

    # Возвращаем количество букв в алфавите
    def letters_num(self):
        return ("Количество букв в данном алфавите равно: " + str(EngAlphabet.__letters_num))


#Русский алфавит
class RusAlphabet(Alphabet):

    

    def __init__(self):
        
        self.alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        super().__init__('Ru', self.alf.upper())

    

    # Проверяем, относится ли буква к русскому алфавиту
    def is_ru_letter(self, letter):
        if letter.upper() in self.letters:
            return ("Буква " + letter + " находится в данном алфавите")
        return ("Буква " + letter + " не находится в данном алфавите")

    # Возвращаем количество букв в алфавите
    def letters_num_ru(self):
        return ("Количество букв в данном алфавите равно: " + str(len(self.alf)))


# Тесты
if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('D'))
    print(eng_alphabet.is_en_letter('О'))

    ru_alphabet = RusAlphabet()
    ru_alphabet.print()
    print(ru_alphabet.letters_num_ru())
    print(ru_alphabet.is_ru_letter('F'))
    print(ru_alphabet.is_ru_letter('Щ'))