#! python3

"""
Simeon Patton
CS362 Oregon State - Spring 2021
In class activity week 8

Apply the following steps to the leap year code in Homework - 1
    1.Write tests for leap year program before you begin implementation.
    2.Make a commit.
    3.Write code and then run the test - then make a commit.
    4.Document Output with unittest.

"""

import unittest
import leap_year

class testCaseVolume(unittest.TestCase):
    ## this test should pass, testing the actual arithmetic of the function
    def test_data_type(self):
        self.assertTrue(type(leap_year.user_input) is int)


if __name__ == '__main__':
    unittest.main()