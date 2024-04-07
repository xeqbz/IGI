# Program: Organize a loop that takes integers and calculates the arithmetic mean of even numbers. End - input 1
# Version: 1.0
# Author: Tsaruk V.
# Date: 01.04.2024

def is_size(value):
    """Checks the value to be greater than 0"""
    while True:
        try:
            value = int(value)
            if value > 0:
                return value
            value = input("Value should be greater than 0, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def is_value(value):
    """Checks the value to be a number"""
    while True:
        try:
            value = int(value)
            return value
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def is_command(value):
    """Check the value to be between 0 and 4"""
    while True:
        try:
            value = int(value)
            if 0 < value < 4:
                return value
            value = input("Value should be between 0 and 4, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def input_numbers():
    """Returns a list of numbers"""
    numbers = list()
    while True:
        try:
            number = int(input("Enter a number: "))
            if number == 1:
                break
            numbers.append(number)
        except ValueError:
            number = input("Invalid input, please enter a valid value: ")
            if number == 1:
                break
    return numbers


def get_size():
    """Returns the number that will be a size of the list"""
    return is_size(input("Enter the size of the list: "))


def generator():
    """Returns a sequence of numbers"""
    while True:
        value = is_value(input("Enter a number: "))
        if value == 1:
            break
        yield value


def find_minimum(args: list):
    """Returns the minimum number from list"""
    return min(args)


def output_minimum(args):
    """Output the minimum number from list"""
    print(f"\nMinimum number from list: {find_minimum(args)}\n")


def menu():
    """Returns menu"""
    print("\n1: Find minimum for 1 series of numbers")
    print("2: Find minimum for several series of numbers")
    print("3: Exit")


def program():
    """Returns the context menu"""
    while True:
        menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            new_list = input_numbers()
            output_minimum(new_list)
        if command == 2:
            size = get_size()
            for _ in range(size):
                k = generator()
                output_minimum(k)
        if command == 3:
            break
