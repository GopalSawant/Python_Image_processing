import unittest
from BulitInModuleGame1 import luck_check


class TestGame(unittest.TestCase):
    def invalid_number(self):
        param1 = 5
        param2 = 5
        result = luck_check(param1, param2)
        self.assertTrue(result)


unittest.main()
