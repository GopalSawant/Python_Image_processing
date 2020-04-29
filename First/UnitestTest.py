import unittest
import UnitestFunc


class TestUnitestFunc(unittest.TestCase):
    print(__name__)

    def test_do_stuff_calculation(self):
        test_param = (10)
        result = UnitestFunc.do_stuff(test_param)
        self.assertEqual(result, 15,'calculation of two number')

    def test_do_stuff_string(self):
        test_param = 'sfdgd'
        result = UnitestFunc.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff_division(self):
        test_param=10/0.01
        result = UnitestFunc.do_stuff(test_param)
        self.assertIsInstance(result,ZeroDivisionError )

    def test_do_stuff_None(self):
        test_param=None
        result = UnitestFunc.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

unittest.main()