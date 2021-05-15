#! python3
"""
Simeon Patton
Inclass activity Week 7
CS362 - OSU Spring 2021

Palindrome -    1. Ask the user for a string and determine whether it is a palindrome or not. 
                2. Write tests for the above specification using unittest and pytest.
                3. Document the outputs in a pdf - (screenshots of the output from unittest and pytest)

    Some code inspiration from www.shorturl.at/eglJ6  

"""

import unittest
import palindrome

## UnitTest Module
class testCaseVolume(unittest.TestCase):
##Unit Test  
##Testing pass and fail of the input type
    ## Testing to see if the input is a type value of "string"
    def test_type(self):
      self.assertTrue(type(palindrome.user_input) is str)
    ## This test should fail as the input type IS string
    def test_type_fail(self):
      self.assertTrue(type(palindrome.user_input) is not str)


if __name__ == '__main__':
    ## UnitTest Module
    unittest.main()