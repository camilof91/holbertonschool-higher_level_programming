#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    '''
    Prints "My name is <first_name> <last_name>".

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
    '''
    # Check if first_name is a string
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    # Print the message with first_name and last_name
    print("My name is {} {}".format(first_name, last_name))

# Test the function with provided examples
say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")

# Test for TypeError exception
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)
