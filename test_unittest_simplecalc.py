# Lets create Test to see if code will be running without any errors

from simple_calc import SimpleCalc
# importing the file where we would write our code
import unittest
# importing unittest to inherit TestCase to create our tests against the code


class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):     # Naming convention - using "test" before or after when naming our function will let python interpreter know that this needs to be tested
        self.assertEqual(self.calc.add(2, 4), 6) # This test is checking "2 + 4 = 6", if true it will pass

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)
        # This test is checking if "4 - 2 = 2", if true it will pass

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        # This test will check if 2 x 2 = 4

    def test_divide(self):
        self.assertEqual(self.calc.divide(15, 3), 5)
        # This test will check "15 / 3 = 5"