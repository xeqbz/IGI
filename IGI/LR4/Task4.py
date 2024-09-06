# Program: Constructs a regular pentagon with side a.
# Version: 1.0
# Author: Tsaruk V.
# Date: 16.04.2024

from abc import ABC, abstractmethod
import math
import matplotlib.pyplot as plt
import numpy as np


class GeometricFigure(ABC):
    """Abstract class """
    @abstractmethod
    def calculate_area(self):
        """ Abstract method for calculating area"""
        pass


class ResizableMixin:
    def resize(self, length):
        self.side_length = length


class Color:
    """ Class for color """
    def __init__(self, color):
        self.color = color


class RegularPentagon(GeometricFigure, ResizableMixin):
    """ Class for regular pentagon """
    def __init__(self, side_length, color, text):
        """ Create regular pentagon with written parameters """
        self.side_length = side_length
        self.color = Color(color)
        self._name = "Regular Pentagon"
        self.text = text

    def calculate_area(self):
        """ Calculate area of regular pentagon """
        return (math.sqrt(25 + 10 * math.sqrt(5)) / 4) * self.side_length ** 2

    @property
    def name(self):
        """ Get name """
        return self._name

    @name.setter
    def name(self, name):
        """ Set name """
        self._name = name

    def __str__(self):
        """ Returns info about figure """
        return "Figure: {}, Color: {}, Area: {:.2f}, Text: {}".format(self.name, self.color.color,
                                                                      self.calculate_area(), self.text)

    def draw(self):
        """ Draws regular pentagon """
        angles = np.linspace(0, 2 * np.pi, 6)[:-1]
        x_cords = self.side_length * np.cos(angles)
        y_cords = self.side_length * np.sin(angles)

        x_cords = np.append(x_cords, x_cords[0])
        y_cords = np.append(y_cords, y_cords[0])

        plt.fill(x_cords, y_cords, color=self.color.color)
        plt.text(0, 0, self.text, horizontalalignment='center', verticalalignment='center')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Regular Pentagon')

        plt.axis('equal')
        plt.grid(True)
        plt.savefig("plot_task4.png")
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


def menu():
    """ Returns menu """
    print("\n1:Show info about figure.")
    print("2:Draw figure.")
    print("3:Exit.")


def is_color(value):
    while True:
        try:
            if value in ['red', 'blue', 'green', 'yellow', 'black']:
                return value
            value = input("Wrong input! Acceptable colors: 'red', 'blue', 'green', 'yellow', 'black'")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def is_value(value):
    """Checks the value to be more than 0"""
    while True:
        try:
            value = float(value)
            if value > 0:
                return value
            value = input("Value should be more than 0, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def program():
    """ Returns context menu """
    figure = RegularPentagon(is_value(input("\nInput size length: ")), is_color(input("Input color: ")),
                             input("Input text to show in figure: "))
    while True:
        menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            print(figure)
        if command == 2:
            figure.draw()
        if command == 3:
            break


if __name__ == '__main__':
    program()
