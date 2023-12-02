import re
file_name = "input.txt"

# Read file input.txt and store it in a list
with open(file_name, "r") as f:
    data = f.readlines()


def remove_non_numeric_characters(raw_lines: str):
    """Removes all non numeric characters from a list of strings"""
    return [re.sub(r'[^0-9]', '', line) for line in raw_lines]

def find_first_and_last_number(lines: str):
    numbers = []
    # Loop through each line and add the first and last number
    for line in lines:
        first_num = line[0]
        last_num = line[-1]
        numbers.append(first_num + last_num)

    total = sum([int(i) for i in numbers])
    return total

if __name__ == "__main__":
    # find the sum of all numbers in the list
    sanitized_data = remove_non_numeric_characters(data)
    solution = find_first_and_last_number(sanitized_data)
    print(solution)