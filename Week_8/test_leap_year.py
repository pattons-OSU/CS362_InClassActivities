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
import pytest
import leap_year

#################UNITTEST########################
user_input = leap_year.user_input()

class testCaseVolume(unittest.TestCase):
    ## this test should pass, testing the actual arithmetic of the function
    def test_data_type(self):
        self.assertTrue(type(user_input) is int)

################PYTEST##########################
@pytest.fixture
def user_input():
    ##user_input = leap_year.user_input()
    user_input = 45343243432
    return user_input

## Pytest, testing to see if user input is a string and not another data type
def test_type(user_input):
    assert type(user_input) is int

if __name__ == '__main__':
    ## UnitTest
    unittest.main()

    ## PyTest
    test_type(leap_year.user_input())
