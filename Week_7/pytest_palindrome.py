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

user_input = "hello world"


##PyTest Module
##user_input = palindrome.user_input()


def test_type(user_input):
    assert type(user_input) is str


if __name__ == '__main__':


    test_type(user_input)