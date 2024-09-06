# Program: Find the maximum modulus element of the list and the sum of the elements of the list located before the last
# positive element
# Version: 1.0
# Author: Tsaruk V.
# Date: 01.04.2024


from Task2 import is_command, get_size, is_size
import math


def is_value(value):
    """Checks the value to be a number"""
    while True:
        try:
            value = float(value)
            return value
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def get_list(size: int):
    """ Returns the sequence of numbers """
    new_list = list()
    for _ in range(size):
        number = is_value(input("Enter a number: "))
        new_list.append(number)
    return new_list


def find_maximum_modulo_element(numbers: list):
    """ Returns the maximum modulo element """
    new = numbers[:]
    for i in range(len(new)):
        if new[i] < 0:
            new[i] = math.fabs(new[i])
    return max(new)


def find_sum_before_last_positive(numbers: list):
    last_positive_index = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            last_positive_index = i
    sum_last_positive = 0
    for i in range(last_positive_index):
        sum_last_positive += numbers[i]
    return sum_last_positive


def output(numbers: list):
    """ Returns the result """
    print(f"\nMaximum modulo element: {find_maximum_modulo_element(numbers)}")
    print(f"The sum of the elements of the list located before the last positive element:"
          f" {find_sum_before_last_positive(numbers)}")


def generator(size: int):
    """ Returns a list of sequences """
    for _ in range(size):
        size_list = is_size(input("Enter the size of the list: "))
        yield get_list(size_list)


def output_series(*lists: list):
    """ Returns result for each strings """
    for numbers in lists:
        output(numbers)


def menu():
    """ Returns menu"""
    print("\n1: Complete task for one series numbers")
    print("2: Complete task for several series numbers")
    print("3: Exit\n")


def program():
    """ Returns the context menu """
    while True:
        menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            size = get_size()
            numbers = get_list(size)
            output(numbers)
        if command == 2:
            size_series = get_size()
            numbers = generator(size_series)
            output_series(*numbers)
        if command == 3:
            break
