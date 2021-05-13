#! python3

"""
Simeon Patton
Inclass activity Week 7
CS362 - OSU Spring 2021

Palindrome -    1. Ask the user for a string and determine whether it is a palindrome or not. 
                2. Write tests for the above specification using unittest and pytest.
                3. Document the outputs in a pdf - (screenshots of the output from unittest and pytest)

"""

def user_input():
    usr_input = input("\nPlease enter a word or string to check:\n")
    return usr_input

string = user_input()

def pal_check(string):
    return string == string[::-1]



if __name__ == "__main__":
    string = user_input()
    ans = pal_check(string)

    if ans:
        print("yes")
    else:
        print("no") 