# Lets create Test to see if code will be running without any errors

from simple_calc import SimpleCalc:
# importing the file where we would write our code
import unittest
# importing unittest to inherit TestCase to create our tests against the code


class CalcTest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):     # Naming convention - using "test" before or after when naming our function will let python interpreter know that this needs to be tested
        # 2 + 2 = 4 = True