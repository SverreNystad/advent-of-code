import re
from part_1 import find_first_and_last_number, remove_non_numeric_characters

def convert_string_numbers_to_digits(string: str):
    """Converts all string numbers to digits"""
    string = string.lower()
    # The mapping of words to digits with the word on both sides so other mappings don't interfere e.i "eightwo" will create "82" instead of "eigh2"
    mapping = {
        "zero": "zero0zero",
        "one": 'one1one', 
        "two": 'two2two', 
        "three": 'three3three', 
        "four": 'four4four', 
        "five": 'five5five',
        "six": 'six6six',
        "seven": 'seven7seven',
        "eight": 'eight8eight',
        "nine": 'nine9nine',
    }

    # Loop through each word in the string
    for number in mapping:
        # Replace all words in mapping with their corresponding digit
        string = string.replace(number, mapping[number])
    return string

if __name__ == "__main__":
    file_name = "input.txt"

    # Read file input.txt and store it in a list
    with open(file_name, "r") as f:
        data = f.readlines()

    converted_lines = [convert_string_numbers_to_digits(line) for line in data]
    converted_lines = remove_non_numeric_characters(converted_lines)
    # Remove all non numeric characters
    solution = find_first_and_last_number(converted_lines)
    print(solution)