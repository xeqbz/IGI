# Program: Determine the number of words in a string and display all words with an odd numbers of letters, find the
# shortest word which start with 'i', display repeated words
# Version: 1.0
# Author: Tsaruk V.
# Date: 01.04.2024


main_string = ("So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy"
               " and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and"
               " picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.")


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


def number_of_words():
    """ Returns number of words """
    words = main_string.split(" ")
    return len(words)


def find_odd_words():
    """ Finds words with odd number of letters """
    string = main_string.replace(",", "")
    string = string.replace("-", " ")
    k = [word for word in string.split(" ") if len(word) % 2 != 0]
    return k


def output_odd_words(*values):
    """ Output words with odd number of letters """
    print(*values, sep=" ")


def find_longest_i_word():
    """ Finds the shortest word which starts with 'i' """
    i = [word for word in main_string.split(" ") if ("i" in word or "I" in word)]
    return min(i, key=len)


def output_longest_i_word(word):
    """ Prints the shortest word which starts with 'i' """
    print(f"\nThe shortest word which starts with \"i\": {word}")


def find_repeated_words():
    """ Finds repeated words """
    string = main_string.replace(",", "")
    string = string.replace("-", " ")
    string = string.lower()
    string = string.split(" ")
    count = {}
    for word in string:
        if count.get(word, None):
            count[word] += 1
        else:
            count[word] = 1
    return dict(count)


def output_repeated_words(words: dict):
    """ Prints repeated words """
    print("\nRepeated words: ")
    k = []
    for key, value in words.items():
        if value > 1:
            k.append(key)
        else:
            continue
    print(*k, sep=" ")


def menu():
    """ Returns menu """
    print("\n1: Complete task")
    print("2: Exit")


def program():
    """ Returns the context menu """
    while True:
        menu()
        command = is_command(input("\nEnter a value: "))
        if command == 1:
            print(f"\nNumber of words: {number_of_words()}\n")
            output_odd_words(*find_odd_words())
            output_longest_i_word(find_longest_i_word())
            output_repeated_words(find_repeated_words())
        if command == 2:
            break
