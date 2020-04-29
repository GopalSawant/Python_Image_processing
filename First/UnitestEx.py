import unittest


class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('setUP')

    def any_test(self):
        print('test')

    def tearDown(self):
        print('tearDown')


unittest.main()
