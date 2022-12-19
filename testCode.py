import unittest
import prog as app

class TestMyProga(unittest.TestCase):
    def setUp(self):
        self.app = app

    def testP(self):
        # Перевірка на виведення правильно результату
        self.assertEqual(app.obchusl("4"), 50)

        # # Перевірка на введення не коректинх данних
        # self.assertEqual(app.obchusl("d"), "ValueError")
        

if __name__ == "__main__":
    unittest.main()
