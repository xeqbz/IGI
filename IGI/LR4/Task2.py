# Program: Text analysis program.
# Version: 1.0
# Author: Tsaruk V.
# Date: 16.04.2024
import re
from zipfile import ZipFile


class Text:
    """ Class for text analysis """

    def __init__(self, filename):
        """ Performs text analysis tasks when creating a class object """
        with open(filename, 'r', encoding='utf-8') as f:
            self.text = f.read()

        self.sentences = len(re.findall(r'[.!?]', self.text))
        self.dots = len(re.findall(r'\.', self.text))
        self.exclamations = len(re.findall(r'!', self.text))
        self.questions = len(re.findall(r'\?', self.text))
        self.avg_sentence_length = self.average_sentence_length()
        self.avg_word_length = self.average_word_length()
        self.emoticons = len(re.findall('[;:]-*[(\[)\]]+', self.text))

        self.less_five = set(self.less_than_five())
        self.highlighted_pairs = re.sub(r'([a-z][A-Z])', r'_?\1?_', self.text)
        self.even_words = self.even_letters_words()
        self.even_words_length = len(self.even_words)
        self.shortest_a = self.shortest_word_starting_with_a()
        self.duplicate_words = self.repeated_words()

    def average_sentence_length(self):
        """ Counts average sentence length """
        sentences = re.split(r'[.!?]', self.text)

        total_chars = 0
        for sentence in sentences:
            words = sentence.split()
            total_chars += sum(len(word) for word in words)

        if len(sentences) != 0:
            average_sentence_length = total_chars / len(sentences)
        else:
            average_sentence_length = 0

        return average_sentence_length

    def average_word_length(self):
        """ Counts average word length """
        words = re.findall(r'\b\w+\b', self.text.lower())

        total_chars = 0
        total_words = len(words)

        for word in words:
            total_chars += len(word)

        if total_words != 0:
            average_word_length = total_chars / total_words
        else:
            average_word_length = 0

        return average_word_length

    def less_than_five(self):
        """ Counts the number of words whose length is less than 5 """
        words = re.findall(r'\b\w+\b', self.text.lower())
        short_words = [word for word in words if len(word) < 5]
        return short_words

    def even_letters_words(self):
        """ Returns words with an even number of letters """
        words = re.findall(r'\b\w+\b', self.text.lower())
        even_words = [word for word in words if len(word) % 2 == 0]
        return even_words

    def shortest_word_starting_with_a(self):
        """ Returns the shortest word that starts with a """
        words = re.findall(r'\b\w+\b', self.text.lower())
        a_words = [word for word in words if word.lower().startswith('a') and len(word) > 1]
        shortest_word = min(a_words, key=len) if a_words else None
        return shortest_word

    def repeated_words(self):
        """ Returns duplicate words """
        words = re.findall(r'\b\w+\b', self.text.lower())
        word_count = {}

        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        duplicate_words = [word for word, count in word_count.items() if count > 1]
        return duplicate_words

    def print_general(self):
        """ Prints general tasks in console: """
        print(f"\nNumber of sentences in the text: {self.sentences};\n\t-declarative sentences: {self.dots};"
              f"\n\t-incentive sentences: {self.exclamations};\n\t-interrogative sentences: {self.questions};")
        print(f"Average sentence length in chars: {self.average_sentence_length()};")
        print(f"Average word length in chars: {self.average_word_length()};")
        print(f"Number of emoticons: {self.emoticons}")

    def print_variant(self):
        """ Prints variant tasks in console: """
        print("\nAll words with length less than 5:", end=' ')
        print(','.join(map(str, self.less_five)))
        print(f"Text with highlighted pairs:\n-----\n{self.highlighted_pairs}\n-----\n")
        print(f"Number of even letters words: {self.even_words_length}")
        print("Even letters words:", end=' ')
        print(','.join(map(str, self.even_words)))
        print(f"Shortest word starting with a: {self.shortest_a}")
        print("Repeated words:", end=' ')
        print(','.join(map(str, self.repeated_words())))


class Files:
    """ Provides functions to word with files """
    @staticmethod
    def write_in_file(my_text: Text, filename):
        """ Writes the results to a file """
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(
                f"Number of sentences in the text: {my_text.sentences};\n\t-declarative sentences: {my_text.dots};"
                f"\n\t-incentive sentences: {my_text.exclamations};\n\t-interrogative sentences: {my_text.questions};")
            f.write(f"\nAverage sentence length in chars: {my_text.average_sentence_length()};")
            f.write(f"\nAverage word length in chars: {my_text.average_word_length()};")
            f.write(f"\nNumber of emoticons: {my_text.emoticons}")
            f.write("\nAll words with length less than 5:")
            f.write(','.join(map(str, my_text.less_five)))
            f.write(f"\nText with highlighted pairs:\n-----\n{my_text.highlighted_pairs}\n-----\n")
            f.write(f"Number of even letters words: {my_text.even_words_length}")
            f.write("\nEven letters words:")
            f.write(','.join(map(str, my_text.even_words)))
            f.write(f"\nShortest word starting with a: {my_text.shortest_a}")
            f.write("\nRepeated words:")
            f.write(','.join(map(str, my_text.repeated_words())))

    @staticmethod
    def archiving(filename):
        """ Archives file """
        with ZipFile("my_archive.zip", 'a') as my_zip:
            my_zip.write(filename, arcname=filename)

    @staticmethod
    def get_info(filename):
        """ Returns info about archive """
        with ZipFile(filename, "r") as my_zip:
            for item in my_zip.infolist():
                print(f"File Name: {item.filename} Date: {item.date_time} Size: {item.file_size}")


def is_command(value):
    """ Checks the value to be between 0 and 5 """
    while True:
        try:
            value = int(value)
            if 0 < value < 5:
                return value
            value = input("Value should be between 0 and 5, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def menu():
    """ Returns menu """
    print("\n1:General task")
    print("2:Personal task")
    print("3:Add output to archive and show info about archive")
    print("4:Exit")


def program():
    """ Returns the context menu """
    my_string = Text('input_task2.txt')
    Files.write_in_file(my_string, 'output_task2.txt')
    while True:
        menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            my_string.print_general()
        if command == 2:
            my_string.print_variant()
        if command == 3:
            Files.archiving('output_task2.txt')
            Files.get_info('my_archive.zip')
        if command == 4:
            break


if __name__ == '__main__':
    program()
