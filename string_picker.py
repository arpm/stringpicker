#!/usr/bin/env python

"""Outputs a list of randomly selected strings given the name of an
input file, the number of strings desired and the number of strings
per line desired"""

import random
import sys

DIGITS_FORMAT = {1: "{:0>1} ", 2: "{:0>2} ", 3: "{:0>3} ", 4: "{:0>4} ",
                 5: "{:0>5} ", 6: "{:0>6} ", 7: "{:0>7} ", 8: "{:0>8} "}


def file_to_list(inputFile):
    """Returns the input file as a list"""
    file = open(inputFile, 'r')
    strings = [line.rstrip() for line in file]
    file.close()
    return strings


def longest_string_length(inputList):
    """Returns the length of the longest string from the input list"""
    return len(max(inputList, key=len))


def string_picker(inputFile, numberOfStrings, stringsPerLine):
    """Returns the randomly selected strings as a formatted string"""

    inputList = file_to_list(inputFile)

    selectedStrings = random.sample(inputList, numberOfStrings)
    longestStringLength = longest_string_length(selectedStrings)
    numberOfDigits = len(str(numberOfStrings))

    outputString = ""

    for string in selectedStrings:

        currentStringLength = len(string)
        currentStringIndex = selectedStrings.index(string)
        currentStringNumber = DIGITS_FORMAT[numberOfDigits].format(
                              currentStringIndex + 1)
        padding = (longestStringLength - currentStringLength + 2) * " "

        if currentStringIndex % stringsPerLine == 0:
            outputString += "\n"

        outputString += currentStringNumber + string + padding

    outputString += "\n"

    return outputString


if __name__ == "__main__":
    OUTPUT = string_picker(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    print(OUTPUT)
