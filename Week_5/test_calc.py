import unittest
import  calc

class testCaseAdd(unittest.TestCase):
    ## this test should pass
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)

## this test will fail
    def test_add_2(self):
        self.assertEqual(calc.add(1,5), 8)

class testCaseSubtract(unittest.TestCase):
    ## this test should pass
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,5), 5)

## This test will fail
    def test_subtract_2(self):
        self.assertEqual(calc.add(1,5), 8)



if __name__ == '__main__':
    unittest.main()