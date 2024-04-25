# Program: Show possibilities in work with NumPy
# Version: 1.0
# Author: Tsaruk V.
# Date: 16.04.2024
import numpy as np


class NumpyTest:
    """ Class for test NumPy module """
    def __init__(self, n, m):
        """ Makes array of integers with size = n * m """
        self.matrix = np.random.randint(low=-100, high=100, size=(n,m))
        self.new_matrix = None
        print(self.matrix)

    def new_matrix_div_by_max_modus(self):
        """ Returns a new matrix by dividing all elements of the original matrix by its largest element in modulus """
        max_abs_value = np.max(np.abs(self.matrix))
        self.new_matrix = self.matrix / max_abs_value
        print(self.new_matrix)

    def dispersion(self):
        """ Returns dispersion of new matrix rounded by hundreds """
        disp = round(np.var(self.new_matrix), 2)
        print(disp)

    def my_dispersion(self):
        """ Returns hand calculated dispersion rounded by hundreds """
        mean = np.mean(self.new_matrix)
        n = self.new_matrix.size
        squared_diff = np.square(self.new_matrix - mean)
        sum_squared_diff = np.sum(squared_diff)
        disp = round(sum_squared_diff / n, 2)
        print(disp)


def is_value(value):
    """Checks the value to be more than 0"""
    while True:
        try:
            value = int(value)
            if value > 0:
                return value
            value = input("Value should be more than 0, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def is_command(value):
    """Check the value to be between 0 and 3"""
    while True:
        try:
            value = int(value)
            if 0 < value < 3:
                return value
            value = input("Value should be between 0 and 3, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def menu():
    """ Returns menu """
    print("\n1:Start")
    print("2:Exit")


def program():
    """ Returns context menu"""
    while True:
        menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            a = NumpyTest(is_value(input("\nInput n: ")), is_value(input("Input m: ")))
            a.new_matrix_div_by_max_modus()
            a.dispersion()
            a.my_dispersion()
        if command == 2:
            break


if __name__ == '__main__':
    program()
