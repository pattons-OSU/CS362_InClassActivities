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

def user_input():
    ## Taking in user input and returning string value
    usr_input = input("\nPlease enter a word or string to check:\n")
    return usr_input


def pal_check(string):
    ## Taking in "usr_input" as a parameter and checking a boolean return
    ## if the original string is the same as the string in reverse
    return string == string[::-1]



if __name__ == "__main__":

    ## Driver code
    string = user_input()
    ans = pal_check(string)

    if ans:
        print(f"\nYour input of '{string}' is a palendrome.\n")
    else:
        print(f"\nYour input of '{string}' is NOT a palendrome.\n") 