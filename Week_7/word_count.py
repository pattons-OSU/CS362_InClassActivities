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

def user_input():
    ## Taking in user input and returning it for use
    usr_input = input("\nPlease enter a sentence to count:\n")
    return usr_input

def string_split(string):
    ## Breaking user input into separate items and then counting them
    separate = string.split()
    count = len(separate)
    print(f"\nOutput - {count}\n")
    return count

if __name__ == "__main__":
    string = user_input()
    string_split(string)