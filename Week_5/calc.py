#! /usr/bin/env python3

"""
    Simeon Patton
    OSU CS362 Spring 2021
    In class activity 2 - Git in action

        a) Create a caluclator program that handles sum, difference, multiplication, and division.
        Push this program to GitHub in multiple commits.
"""


def calc(a, b):
    sum = a + b
    print(f"The sum of {a} + {b} is {sum}.")
    
    difference = a - b
    print(f"The difference of {a} and {b} is {difference}.")

    multiplication = a * b
    print(f"{a} multipled by {b} is {multiplication}.")

    divide = a / b
    print(f"{a} divided by {b} is {divide}.")

    FinalValues = [sum, difference, multiplication, divide]
    print(f"These values in list form are {FinalValues}.")

    SumOfList = FinalValues[0] + FinalValues[1] + FinalValues[2] + FinalValues[3]
    print(f"The sum of the listed values is {SumOfList}.")

def a_input():
    a = input("Please enter a number 'a': ")
    a = int(a)
    print("")
    return int(a)

def b_input():
    b = input("Please enter a number 'b': ")
    print("")
    b = int(b)
    return int(b)

if __name__ == "__main__":
    print("")
    a = a_input()
    b = b_input()
    calc(a,b)
    print("")