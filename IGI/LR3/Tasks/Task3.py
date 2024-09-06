# Program: In a string entered from the keyboard, count the number of a lowercase letters and numbers
# Version: 1.0
# Author: Tsaruk V.
# Date: 01.04.2024

from Task2 import is_command, is_size


def get_size():
    """ Returns the size of the list """
    return is_size(input("Enter the size: "))


def generator(size: int):
    """ Returns the sequence of strings """
    for _ in range(size):
        yield initialize()


def initialize():
    """ Returns the string """
    return input("Enter the string: ")


def calculate_letters(string):
    """ Counts a number of lowercase letters """
    k = [letter for letter in string if letter.islower()]
    return len(k)


def calculate_numbers(string):
    """ Counts a number of numbers """
    k = [number for number in string if number.isdigit()]
    return len(k)


def output_letters(value):
    """ Prints result """
    print(f"Number of lowercase letters: {value}")


def output_numbers(value):
    """ Prints result """
    print(f"Number of numbers: {value}")


def calculate_several_strings_letters(*string):
    """Counts a number of lowercase letters for several strings"""
    for word in string:
        k = calculate_letters(word)
        yield k


def calculate_several_strings_numbers(*string):
    """Counts a number of numbers for several strings"""
    for number in string:
        k = calculate_numbers(number)
        yield k


def output_several_strings_letters(*values):
    """ Prints result for several strings """
    for letters in values:
        output_letters(letters)


def output_several_strings_numbers(*values):
    """ Prints result for several strings """
    for numbers in values:
        output_letters(numbers)


def menu():
    """ Returns menu """
    print("\n1: Counting a number of lowercase letters and numbers for string")
    print("2: Counting a number of lowercase letters and numbers for strings")
    print("3: Exit")


def program():
    """ Returns the context menu """
    while True:
        menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            string = initialize()
            output_letters(calculate_letters(string))
            output_numbers(calculate_numbers(string))
        if command == 2:
            size = get_size()
            strings = generator(size)
            letters = calculate_several_strings_letters(*strings)
            output_several_strings_letters(*letters)
            numbers = calculate_several_strings_numbers(*strings)
            output_several_strings_numbers(numbers)
        if command == 3:
            break
