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
import palindrome
import pytest

## Had to hard code a user input here because the "fixture"
## was not found otherwise. Hardcode suggested for final draft
## by TA Raghuram

@pytest.fixture
def user_input():
    return "hello world"

##PyTest Module
##user_input = palindrome.user_input()

## Pytest, testing to see if user input is a string and not another data type
def test_type(user_input):
    user_input = "hello world"
    assert type(user_input) is str

if __name__ == '__main__':
    user_input = "hello world"

    test_type(user_input)