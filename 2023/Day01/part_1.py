import re
file_name = "input.txt"

# Read file input.txt and store it in a list
with open(file_name, "r") as f:
    input = f.readlines()


    solution = []
    # Remove all non numeric characters
    lines = [re.sub(r'[^0-9]', '', line) for line in input]

    # Loop through each line and add the first and last number
    for line in lines:
        first_num = line[0]
        last_num = line[-1]
        solution.append(first_num + last_num)


if __name__ == "__main__":
    # find the sum of all numbers in the list
    total = sum([int(i) for i in solution])
    print(total)