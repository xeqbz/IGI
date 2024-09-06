# Program: Calculating the value of a function using a power series expansion of the function
# Version: 1.0
# Author: Tsaruk V.
# Date: 01.04.2024

import math
from prettytable import PrettyTable


table = PrettyTable()


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


def is_eps(value):
    """Checks the value to be between 0 and 1"""
    while True:
        try:
            value = float(value)
            if 0 < value < 1:
                return value
            value = input("Value should be between 0 and 1, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def is_value(value):
    """Checks the value to be less than 1"""
    while True:
        try:
            value = float(value)
            if value < 1:
                return value
            value = input("Value should be less than 1, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def get_size_tuple():
    """Returns the number that will be the size of the list"""
    return is_size(input("Enter size of list: "))


def generator(size: int):
    """Returns a sequence of numbers"""
    for _ in range(size):
        yield is_value(input("Enter values: "))


def get_list(size: int):
    """Returns eps and generator"""
    return is_eps(input("Enter eps: ")), tuple(generator(size))


def get_values():
    """Return eps and value"""
    return is_eps(input("Enter eps: ")), is_value(input("Enter value: "))


def get_taylor_math(x: int):
    """Returns the value of a function using a module math"""
    return math.log(1 + x)


def get_taylor_series(eps: float, x: float):
    """Returns the value of a function using eps"""
    n = 1
    s = 0
    a = x
    while abs(a) > eps and n < 501:
        s += a
        a = float((-1) ** (n - 1) * (x ** n / n))
        n += 1
    s -= x
    return n, s


def add_value(eps: float, value):
    """Adds values to the table"""
    n, s = get_taylor_series(eps, value)
    s_math = get_taylor_math(value)

    table.field_names = ["x", "n", "F(x)", "Math F(x)", "eps"]
    table.add_row([value, n, s, s_math, eps])


def add_tuple(eps: float, *args):
    """Unpacks the tuple and calls the method 'add_value'"""
    for value in args:
        add_value(eps, value)


def output_table():
    """Returns and clear the table"""
    print(table)
    table.clear()


def menu():
    """Return menu"""
    print("\n1: Counting a series for 1 number")
    print("2: Counting a series for several numbers")
    print("3: Exit")


def program():
    """Returns the context menu"""
    while True:
        menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            eps, value = get_values()
            add_value(eps, value)
            output_table()
        if command == 2:
            size = get_size_tuple()
            eps, new_list = get_list(size)
            add_tuple(eps, *new_list)
            output_table()
        if command == 3:
            break
