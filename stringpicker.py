"""Picks random elements of a list given the list itself and the number
of picks desired by the user"""

from random import randint  # imports the random module


def pick_random(input_list, number_of_picks):
    """Picks random elements of an input list given the number of picks"""

    # an empty list where random elements will be added
    selected_strings = []

    # iterates for a number of times to generate random indexes
    for index in range(0, number_of_picks):
        random_index = randint(0, len(input_list) - 1)

        # looks for an empty index in 'selected_list'
        while input_list[random_index] in selected_strings:
            random_index = randint(0, len(input_list) - 1)

        # adds the new random element to 'selected_list'
        selected_strings.append(input_list[random_index])

    return selected_strings


def longest_string(input_list):
    """Returns the longest string of a list"""

    longest = ""

    # iterates through 'selected_list' to determine the longest string in it
    for index in range(0, len(input_list)):
        if len(longest) < len(input_list[index]):
            longest = input_list[index]

    return len(longest)


def format_output(input_list, longest_length, elements_per_line):
    """Formats and print the list of inputs"""

    # an empty string where the selected items will be added to
    output_string = ""

    for index in range(0, len(input_list)):

        # splits every line of output given the 'elements_per_line'
        if index % elements_per_line == 0:
            output_string += "\n"

        # this is the number of spaces required to make the output readable
        number_of_spaces = longest_length - len(input_list[index]) + 2

        # this is the format that is going to be used for the output string
        output_string += ("{:0>2d}".format(index + 1) +
                          " " + input_list[index] +
                          " " * number_of_spaces)

    output_string += "\n"

    return output_string


def string_picker(input_list, number_of_picks, elements_per_line):
    """Does all the magic"""
    selected = pick_random(input_list, number_of_picks)
    longest = longest_string(selected)
    output = format_output(selected, longest, elements_per_line)
    return output


def elements_length_average(input_list):
    """Return the average length of every string element of a list"""
    concatenated = ''.join(input_list)
    concatenated = concatenated.replace(' ', '')
    average = len(concatenated) / float(len(input_list))
    average = "{0:.2f}".format(average)
    return average
