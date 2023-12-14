"""
This list represents the Calories of the food carried by five Elves:

    The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
    The second Elf is carrying one food item with 4000 Calories.
    The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
    The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
    The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask:
they'd like to know how many Calories are being carried by the Elf carrying the most Calories.
In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?


Break down into tasks:
* Read the file line by line
* Convert that list of lines into list[list[int]]
* Convert each of the lists into the sum of the component lists
* Get the maximum of that list and return
"""


def read_file() -> list[str]:
    with open("puzzle_input/day_01.txt", "r") as source_file:
        source_contents = source_file.readlines()
        return [x.strip() for x in source_contents]


def convert_to_list_of_lists(contents: list[str]) -> list[list[int]]:
    result = []
    current_list = []
    for content_line in contents:
        if content_line == '':
            result.append(current_list)
            current_list = []
        else:
            current_list.append(int(content_line))
    result.append(current_list)
    return result


def convert_to_list_of_sums(contents: list[list[int]]) -> list[int]:
    return [sum(x) for x in contents]


if __name__ == '__main__':
    file_contents = read_file()
    list_of_list = convert_to_list_of_lists(file_contents)
    list_of_sums = convert_to_list_of_sums(list_of_list)
    print(max(list_of_sums))
