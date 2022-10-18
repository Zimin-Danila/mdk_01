from библиотека_по_заданию import Reading_rooms
import unittest

class TestLibraries(unittest.TestCase):

    def setUp(self):
        self.b1 = Reading_rooms("Пионерия", "Ленинская", 11589, 150, "8.00 - 19.00", 2, 20)
        self.b2 = Reading_rooms("Пролетариат", "Ленинская", 15860, 200, "8.00 - 21.00", 3, 34)
        self.b3 = Reading_rooms("Свобода", "Капитализм", 8469, 80, "6.00 - 18.00", 15, 15)
        self.b4 = Reading_rooms("Рынок", "Капитализм", 50214, 500, "10.00 - 22.00", 12, 51)
    
    def test_amount_books(self):
        books_libraries = 86132
        self.b1.books_test()
        self.assertEqual(self.b1.books_test(), books_libraries)

if __name__ == '__main__':
    unittest.main()