# TDD
# TEST DRIVEN DEVELOPMENT
### Why should we use TDD?
### What are the benefits of TDD

**Best Use Case**
- We will use PyTest unit-test in Python to implement TDD
- TDD is widely used and is the cheapest way to test code and implement test driven development 

**Best Practices for TDD**
- Write the smallest possible test case that matches what we need to program 
- TDD cycle starts with everything failing  - `RED`
- Write code to pass the test - `GREEN`
- Refactor code for next test - `BLUE`

```python
def greeting(name):
    return "Hello" + name

def thanks(name):
    return "Thank you for visiting " + name
```
**TEST TABLE**

|Method |   Checks that|   New in |
|:---|:---|:---|
|assertEqual(a, b)        | a == b              ||
|assertNotEqual(a, b)     |    a != b              ||  
|assertTrue(x)            |    bool(x) is True     ||  
|assertFalse(x)           |    bool(x) is False    ||  
|assertIs(a, b)           |    a is b             |3.1|
|assertIsNot(a, b)        |    a is not b          |3.1|
|assertIsNone(x)          |    x is None           |3.1|
|assertIsNotNone(x)       |    x is not None       |3.1|
|assertIn(a, b)           |    a in b              |3.1|
|assertNotIn(a, b)        |    a not in b         |3.1|
|assertIsInstance(a, b)   |    isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|    not isinstance(a, b)|3.2|

- Let's create a file called 
`test_unittest_simplecalc.py` 
- Naming is very important as it shows what need to be tested

### SIMPLE CALCULATOR 
- Here we are creating a simple calculator 
- This is our code
```python
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
```
- Next we need to run out test, use use ` python -m pytest` to test code, here is the other file 
```python
class SimpleCalc():  # pass

    def add(self, value1, value2):
        return value1 + value2

    def subtract(self, value1, value2):
        return value1 - value2

    def multiply(self, value1, value2):
        return value1 * value2

    def divide(self, value1, value2):
        return value1 / value2

```
### UNIT TESTING 
- We can unittest by adding `python -m unittest discover -v` in the console
```
test_add (test_unittest_simplecalc.CalcTest) ... ok
test_divide (test_unittest_simplecalc.CalcTest) ... ok
test_multiply (test_unittest_simplecalc.CalcTest) ... ok
test_subtract (test_unittest_simplecalc.CalcTest) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.002s

OK
```