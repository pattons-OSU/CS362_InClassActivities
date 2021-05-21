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

    **Code reused from earlier in semester

"""

## Import os to get the size of the display
import os
display_size = os.get_terminal_size()



def user_input():
    print("")
    in_year = input('Please enter the year that you would like to check: ')
    in_year = int(in_year)
    print("")
    return in_year

## A leap year is a year that is divisible (with no remainder) by 4 (mod 4)
## If the year is evenly divisible by 100 it is not, unless it is simultaneously
## divisible by 400 with no remainder.
def check_year(in_year):
    if (in_year % 4) == 0:
        if(in_year % 100) == 0:
            if(in_year % 400) == 0:
                print(in_year, "is a leap year.")
            else:
                print(in_year, "is not a leap year.")
        else:
            print(in_year, "is a leap year.")
    else:
        print(in_year, "is not a leap year.")
    



if __name__ == "__main__":
    ## Printing display break * size of user display
    print("")
    print("-" * display_size[0])
    
    check_year(user_input())

    print("")
    print("-" * display_size[0])
    print("")   