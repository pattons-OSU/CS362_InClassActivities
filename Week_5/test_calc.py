#! /usr/bin/env python3

import unittest
import  calc

"""
    Simeon Patton
    OSU CS362 Spring 2021
    In class activity 3 - Unit Test

        a) write a simple calc app
        b) your app should take two numbers as imputs (a,b)
        c) should have the following methods:
           addition, subtraction, multiplication, division
        d) Create a test module that has your test cases

        Each test case method has one test that will pass and one that will fail
        This allows us to visualize the difference in the terminal output.
"""

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

class testCaseMultiply(unittest.TestCase):
    ## This test should pass
    def test_multiplication(self):
        self.assertEqual(calc.multiply(5,5), 25)

    ## this test should fail
    def test_multiplication_2(self):
        self.assertEqual(calc.multiply(5,5), 50)

class testCaseDivide(unittest.TestCase):
    ## This test should pass
    def test_divide(self):
        self.assertEqual(calc.divide(25,5), 5)

    ## This test should fail
    def test_divide_2(self):
        self.assertEqual(calc.divide(25,5), 2)

        



if __name__ == '__main__':
    unittest.main()