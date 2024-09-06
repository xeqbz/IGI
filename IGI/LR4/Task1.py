# Program: Program takes surname from keyboard and show information about this student and show list of exams.
# Version: 1.0
# Author: Tsaruk V.
# Date: 16.04.2024
import csv
import pickle


class Students:
    """ Contains list of students"""
    applicants = {
        "Jackson": "Guitar",
        "Miler": "Piano",
        "House": "Piano",
        "Holmes": "Violin",
        "Jordan": "Guitar"
    }

    @staticmethod
    def make_exam_list():
        """ Makes list of exams and students of them"""
        exam_list = {}
        for surname, instrument in CsvStudents.applicants.items():
            if instrument not in exam_list:
                exam_list[instrument] = []
            exam_list[instrument].append(surname)
        return exam_list

    @staticmethod
    def get_info(data, surname):
        """ Returns info about entered student """
        instrument = data.get(surname)
        if instrument:
            print(f"{surname} plays the {instrument}")
        else:
            print(f"{surname} is not found in the list")


class PickleStudents(Students):
    """ Get functions to do task for pickle """
    @staticmethod
    def serialize_pickle(data, filename):
        """ Serialize data in pickle """
        with open(filename, "wb") as f:
            pickle.dump(data, f)

    @staticmethod
    def deserialize_pickle_students():
        """ Deserialize list of students from pickle file """
        with open('students.pickle', "rb") as f:
            data = pickle.load(f)
        return data

    @staticmethod
    def deserialize_pickle_exam_list():
        """ Deserialize exam list from pickle file """
        with open('exam_list.pickle', "rb") as f:
            data = pickle.load(f)
        for instrument, surnames in data.items():
            print(f"Exam Instrument: {instrument}")
            print("Surnames:")
            for surname in surnames:
                print(surname)


class CsvStudents(Students):
    """ Get functions to do task for csv files """
    @staticmethod
    def serialize_csv_students():
        """ Serialize list of students in csv file"""
        with open('students_csv.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["Surname", "MusicalInstrument"], quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for surname, instrument in CsvStudents.applicants.items():
                writer.writerow(dict(Surname=surname, MusicalInstrument=instrument))

    @staticmethod
    def serialize_csv_exam_list(exam_list):
        """ Writes exam list in csv file """
        with open('exam_list.csv', 'w', newline='') as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            writer.writerow(["ExamInstrument", "Surnames"])
            for instrument, surname in exam_list.items():
                writer.writerow([instrument, *surname])

    @staticmethod
    def deserialize_csv_exam_list():
        """ Deserializes exam_list from csv file """
        with open('exam_list.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    print(', '.join(row))

    @staticmethod
    def deserialize_csv_students():
        """ Deserialize list of students from csv file """
        data = {}
        with open('students_csv.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    surname, instrument = row
                    data[surname] = instrument
        return data


def task_menu():
    """ Returns menu for task """
    print("\n1:Show exams list")
    print("2:Show information about student")
    print("3:Exit")


def csv_variant():
    """ Starts task for CSV variant """
    CsvStudents.serialize_csv_students()
    while True:
        task_menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            CsvStudents.serialize_csv_exam_list(CsvStudents.make_exam_list())
            CsvStudents.deserialize_csv_exam_list()
        if command == 2:
            CsvStudents.get_info(CsvStudents.deserialize_csv_students(), input("\nInput surname: "))
        if command == 3:
            break


def pickle_variant():
    """ Start task for pickle variant """
    while True:
        task_menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            PickleStudents.serialize_pickle(PickleStudents.make_exam_list(), 'exam_list.pickle')
            PickleStudents.deserialize_pickle_exam_list()
        if command == 2:
            PickleStudents.serialize_pickle(PickleStudents.applicants, 'students.pickle')
            PickleStudents.get_info(PickleStudents.deserialize_pickle_students(), input("\nInput surname: "))
        if command == 3:
            break


def is_command(value):
    """ Checks the value to be between 0 and 4 """
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
    print("\n1:Start version with CSV files")
    print("2:Start version with picker")
    print("3:Exit")


def program():
    """ Returns the context menu """
    while True:
        menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            csv_variant()
        if command == 2:
            pickle_variant()
        if command == 3:
            break


if __name__ == '__main__':
    program()
