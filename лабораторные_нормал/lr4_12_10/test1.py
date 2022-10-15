from bibl1 import Biblioteki_city
import unittest

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.b1 = Biblioteki_city(1000, 1)
        self.b2 = Biblioteki_city(15087, 2)
        self.b3 = Biblioteki_city(364, 3)
        self.b4 = Biblioteki_city(8564, 4)
    
    def test_account_deposit(self):
        books_city = 25015
        self.b2.books_test()
        self.assertEqual(self.b2.books_test(), books_city)

if __name__ == '__main__':
    unittest.main()