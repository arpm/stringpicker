"""Picks random elements of a list given the list itself and the number
of picks desired by the user"""

import random
import sys


def string_picker(input_list, number_of_picks, elements_per_line):
    """Formats and print the list of inputs"""

    selected = random.sample(input_list, number_of_picks)

    output_string = ""

    for index in range(0, len(selected)):

        # this is the number of spaces required to make the output readable
        spaces = len(max(selected, key=len)) - len(selected[index]) + 2

        # splits every line of output given the 'elements_per_line'
        output_string += "\n" if index % elements_per_line == 0 else ""

        # this is the format that is going to be used for the output
        output_string += ("{:0>2d}".format(index + 1) + " "
                          + selected[index] + " " * spaces)

    output_string += "\n"

    return output_string


if __name__ == "__main__":
    FILE = open(sys.argv[1], 'r')

    QUESTIONS = [line.rstrip() for line in FILE]

    OUTPUT = string_picker(QUESTIONS, int(sys.argv[2]), int(sys.argv[3]))
    print(OUTPUT)
