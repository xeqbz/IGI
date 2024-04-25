# Program: Calculating the value of a function using a power series expansion of the function.
# Version: 1.0
# Author: Tsaruk V.
# Date: 16.04.2024

import math
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt

table_1 = PrettyTable()
table_2 = PrettyTable()


class MyTaylor:
    """ Class for work with taylor series"""
    def __init__(self, x: float, eps: float):
        """ Init result """
        self.x = x
        self.eps = eps
        self.elements = []
        self.answer, self.n = self.result()
        self.m_result = math.log(1 + self.x)

        self.average = sum(self.elements) / self.n
        self.median = self.find_median()
        self.mode = self.find_mode()
        self.dispersion, self.deviation = self.find_dispersion_and_deviation()

    def result(self):
        """ Calculate result with taylor series"""
        n = 1
        s = 0
        a = self.x
        while abs(a) > self.eps and n < 501:
            s += a
            self.elements.append(a)
            a = float((-1) ** (n - 1) * (self.x ** n / n))
            n += 1
        s -= self.x
        del self.elements[0]
        return s, n

    @staticmethod
    def result_static(x, eps=1e-6):
        """ Calculate result with taylor series"""
        arr = []
        for val in x:
            n = 1
            term = val
            sum_term = val
            while abs(term) > eps:
                n += 1
                term *= -val
                term /= n
                sum_term += term
            arr.append(sum_term)
        return arr

    def find_median(self):
        """ Returns median """
        arr = self.elements
        arr.sort()

        n = len(arr)
        if n % 2 == 0:
            median = (arr[n // 2 - 1] + arr[n // 2]) / 2
        else:
            median = arr[n // 2]

        return median

    def find_mode(self):
        """ Returns mode """
        count_dict = {}
        for item in self.elements:
            count_dict[item] = count_dict.get(item, 0) + 1
        mode = max(count_dict, key=count_dict.get)

        return mode

    def find_dispersion_and_deviation(self):
        """ Returns dispersion and standard deviation"""
        mean = sum(self.elements) / len(self.elements)
        deviations = [(x - mean) ** 2 for x in self.elements]
        dispersion = sum(deviations) / len(self.elements)
        std_dev = math.sqrt(dispersion)
        return dispersion, std_dev

    def output_result_table(self):
        """ Output table with results """
        table_1.field_names = ["x", "n", "F(x)", "Math F(x)", "eps"]
        table_1.add_row([self.x, self.n, self.answer, self.m_result, self.eps])
        print(table_1)
        table_1.clear()

    def output_additional_table(self):
        """ Output table with additional results """
        table_2.field_names = ["average", "median", "mode", "dispersion", "standard deviation"]
        table_2.add_row([self.average, self.median, self.mode, self.dispersion, self.deviation])
        print(table_2)
        table_2.clear()

    @staticmethod
    def draw_plot():
        """ Draws plot and save it to file """
        x = np.linspace(0.1, 0.9, 100)
        y1 = np.log(1 + x)
        y2 = MyTaylor.result_static(x)

        plt.plot(x, y1, color='blue', label='y = log(1 + x)(math)')
        plt.plot(x, y2, color='red', label='y = log(1 + x)(Taylor)')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Function graphs')
        plt.grid(True)
        plt.legend()
        plt.savefig("plot_task3.png")
        plt.show()


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


def menu():
    """ Returns menu """
    print("\n1:Print results.")
    print("2:Print plots.")
    print("3:Exit")


def program():
    """ Returns context menu """
    while True:
        menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            var = MyTaylor(is_value(input("Enter value: ")), is_eps(input("Enter eps: ")))
            var.output_result_table()
            var.output_additional_table()
        if command == 2:
            MyTaylor.draw_plot()
        if command == 3:
            break


if __name__ == '__main__':
    program()
