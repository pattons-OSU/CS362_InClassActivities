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
import word_count
import pytest

## I was forced to hardcode the input on this one too as the pytest
## module would not allow the user to input into the program eventhough
## it was called as seen below
@pytest.fixture
def user_input():
    ##user_input = word_count.user_input()
    user_input = "Hello I had to hardcode this too"
    return user_input

## Pytest, testing to see if user input is a string and not another data type
def test_type(user_input):
    assert type(user_input) is str

if __name__ == '__main__':
    test_type(user_input)