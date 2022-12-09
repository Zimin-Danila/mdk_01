import sqlite3

con = sqlite3.connect("C:\Programming\mdk_01\лабораторные_нормал\lr28_08_12\database.db")
con.execute("PRAGMA foreign_keys = 1")

cursor = con.cursor()

def create_table_libraries() -> None:
    """Таблица, хранящая название, адрес и город библиотеки"""
    req = """
    CREATE TABLE IF NOT EXISTS Libraries(
    name TEXT PRIMARY KEY,
    adress TEXT,
    city TEXT)"""
    cursor.execute(req)
    con.commit()

        # Создание новой строки для 4-го пункта задания
# cursor.execute("INSERT INTO Libraries (name, adress, city) VALUES ('Краснознаменная', 'улица Иногородняя 86', 'Молотов')")
# con.commit()

        # Обновление строки для 4-го задания
# cursor.execute("UPDATE Libraries SET city='Пермь' WHERE city='Молотов'")
# con.commit()

        # Удаление этой строки
# cursor.execute("DELETE FROM Libraries WHERE name=?", ('Краснознаменная',))
# con.commit()

        # Проверка
cursor.execute("SELECT * FROM Libraries")
print(cursor.fetchall())





# libraries_input = [("Мироздание", "проспект Мира 25", "Севастополь"), 
#                   ("Бумажково", "улица Бассейная 10", "Сковородкино")]
# cursor.executemany("INSERT INTO Libraries (name, adress, city) VALUES (?, ?, ?)", libraries_input)
# con.commit()


def create_table_reading_rooms() -> None:
    """Таблица, хранящая название читательного зала, название библиотеки, 
    количество единиц литературы, количество посадочных мест, время работы, 
    этаж, количество сотрудников"""
    req ="""
    CREATE TABLE IF NOT EXISTS Reading_rooms(
    name TEXT PRIMARY KEY,
    name_library TEXT, 
    number_literature INTEGER,
    number_seats INTEGER,
    opening_hours TEXT,
    floor INTEGER,
    number_employees INTEGER,
    FOREIGN KEY (name_library) REFERENCES Libraries (name))"""
    cursor.execute(req)
    con.commit()

# reading_rooms_input = [("Основатель", "Мироздание", 1498, 500, "8.00 - 19.00", 3, 14), 
#                       ("Подмастерье", "Бумажково", 634, 250, "8.00 - 19.00", 9, 8)]
# cursor.executemany("INSERT INTO Reading_rooms (name, name_library, number_literature, \
# number_seats, opening_hours, floor, number_employees) VALUES (?, ?, ?, ?, ?, ?, ?)", reading_rooms_input)
# con.commit()

def create_table_reader() -> None:
    """Таблица, хранящая фамилию, имя, отчество, 
    категорию читателя, место работы или учёбы, 
    возраст и дату регистрации в библиотеке"""
    req ="""
    CREATE TABLE IF NOT EXISTS Reader(
    surname TEXT,
    first_name TEXT PRIMARY KEY, 
    patronomyc TEXT,
    category_reader TEXT,
    work_or_study TEXT,
    age INTEGER,
    data_registration TEXT)"""
    cursor.execute(req)
    con.commit()

# reader_input = [("Зимин", "Данила", "Викторович", "Опытный", "Студент", 18, "25.10.2018"), 
#                ("Четырин", "Антон", "Петрович", "Легендарный", "Студент", 17, "20.12.2015")]
# cursor.executemany("INSERT INTO Reader (surname, first_name, patronomyc, \
# category_reader, work_or_study, age, data_registration) VALUES (?, ?, ?, ?, ?, ?, ?)", reader_input)
# con.commit()

def create_table_literature() -> None:
    """Таблица, хранящая название, категорию литературы, 
    авторов, издательство, год издательства, количество страниц, читательный зал"""
    req ="""
    CREATE TABLE IF NOT EXISTS Literature(
    name TEXT PRIMARY KEY,
    category_literature TEXT, 
    authors TEXT,
    publisher TEXT,
    year_publising INTEGER,
    number_pages INTEGER,
    reading_room TEXT,
    FOREIGN KEY (reading_room) REFERENCES Reading_rooms (name))"""
    cursor.execute(req)
    con.commit()

# literature_input = [("Капитал", "Политическая философия, экономика", "Карл Маркс", "Эксмо", 2022, 1200, "Основатель"), 
#                    ("Горячий снег", "Роман", "Юрий Бондарев", "Амфора", 2014, 478, "Подмастерье")]
# cursor.executemany("INSERT INTO Literature (name, category_literature, authors, publisher,\
#      year_publising, number_pages, reading_room) VALUES (?, ?, ?, ?, ?, ?, ?)", literature_input)
# con.commit()

def create_table_literature_otput() -> None:
    """Таблица, хранящая имя читателя, название литературы, дату выдачи, срок выдачи, вид выдачи, наличие залога"""
    req ="""
    CREATE TABLE IF NOT EXISTS Literature_output(
    name_reader TEXT,
    name_literature TEXT, 
    date_issue TEXT,
    period_issue TEXT,
    type_issue TEXT,
    guarantee TEXT,
    FOREIGN KEY (name_reader) REFERENCES Reader (first_name),
    FOREIGN KEY (name_literature) REFERENCES Literature(name))"""
    cursor.execute(req)
    con.commit()

# literature_output_input = [("Данила", "Капитал", "01.12.2022", "6 месяцев", "Лично", "Наличие залога"), 
#                           ("Антон", "Горячий снег", "27.08.2022", "2 месяца", "Онлайн", "Отсутствие залога")]
# cursor.executemany("INSERT INTO Literature_output (name_reader, name_literature, date_issue, period_issue,\
#      type_issue, guarantee) VALUES (?, ?, ?, ?, ?, ?)", literature_output_input)
# con.commit()


# create_table_libraries()
# create_table_reading_rooms()
# create_table_reader()
# create_table_literature()
# create_table_literature_otput()