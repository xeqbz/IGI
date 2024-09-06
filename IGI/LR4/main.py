import Task1
import Task2
import Task3
import Task4
import Task5


def is_command(value):
    """ Checks the value to be between 0 and 7 """
    while True:
        try:
            value = int(value)
            if 0 < value < 7:
                return value
            value = input("Value should be between 0 and 7, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def menu():
    """ Returns menu """
    print("\n1:Start Task1")
    print("2:Start Task2")
    print("3:Start Task3")
    print("4:Start Task4")
    print("5:Start Task5")
    print("6:Exit")


def program():
    while True:
        menu()
        command = is_command(input("\nEnter value: "))
        if command == 1:
            Task1.program()
        if command == 2:
            Task2.program()
        if command == 3:
            Task3.program()
        if command == 4:
            Task4.program()
        if command == 5:
            Task5.program()
        if command == 6:
            break


if __name__ == '__main__':
    program()
