#! python3
"""
Simeon Patton
Inclass activity Week 7
CS362 - OSU Spring 2021

Word Count-
        1. Ask the user for a sentence and determine the number of
        words in that sentence.
        Example - “This is an activity”, Output - 4.
        2. Write tests for the above specification using unittest and
        pytest.
        3. Document the outputs in a pdf - (screenshots of the output
        from unittest and pytest)    
"""
import unittest
import word_count


class testCaseVolume(unittest.TestCase):
##Unit Test  
##Testing pass and fail of the input type
    ## Testing to see if the input is a type value of "string"
    def test_type(self):
      self.assertTrue(type(word_count.user_input) is str)
    ## This test should fail as the input type IS string
    def test_type_fail(self):
      self.assertTrue(type(word_count.user_input) is not str)

if __name__ == '__main__':
    unittest.main()