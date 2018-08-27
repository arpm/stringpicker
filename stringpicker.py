#!/usr/bin/env python

"""Picks random elements of a list given the list itself and the number
of picks desired by the user"""

import random
import sys


def longest_string_length(inputList):
    return len(max(inputList, key=len))


def file_to_list(inputFile):
    file = open(inputFile, 'r')
    questions = [line.rstrip() for line in file]
    return questions


def string_picker(inputFile, numberOfPicks, elementsPerLine):
    """Formats and print the list of inputs"""

    inputList = file_to_list(inputFile)

    selected = random.sample(inputList, numberOfPicks)
    longestStringLength = longest_string_length(selected)

    outputString = ""

    for question in selected:

        currentStringLength = len(question)
        currentStringIndex = selected.index(question)
        currentStringNumberFormat = "{:0>2} ".format(currentStringIndex + 1)
        padding = (longestStringLength - currentStringLength + 2) * " "

        if currentStringIndex % elementsPerLine == 0:
            outputString += "\n"

        outputString += currentStringNumberFormat + question + padding

    outputString += "\n"

    # for index in range(0, len(selected)):

    #     current_string_length = len(selected[index])

    #     # this is the number of spaces required to make the output readable
    #     spaces =  longest_string_length - current_string_length + PADDING

    #     # splits every line of output given the 'elementsPerLine'
    #     output_string += "\n" if index % elementsPerLine == 0 else ""

    #     # this is the format that is going to be used for the output
    #     output_string += ("{:0>2d}".format(index + 1) + " "
    #                       + selected[index] + " " * spaces)

    return outputString


if __name__ == "__main__":
    OUTPUT = string_picker(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    print(OUTPUT)
