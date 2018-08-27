#!/usr/bin/env python

"""Outputs a list of randomly selected strings given the name of an
input file, the number of strings desired and the number of strings
per line desired"""

import random
import sys


def file_to_list(inputFile):
    """Returns the input file as a list"""
    file = open(inputFile, 'r')
    strings = [line.rstrip() for line in file]
    file.close()
    return strings


def longest_string_length(inputList):
    """Returns the length of the longest string from the input list"""
    return len(max(inputList, key=len))


def string_picker(inputFile, numberOfPicks, stringsPerLine):
    """Returns the randomly selected strings as a formatted string"""

    inputList = file_to_list(inputFile)

    selectedStrings = random.sample(inputList, numberOfPicks)
    longestStringLength = longest_string_length(selectedStrings)

    outputString = ""

    for string in selectedStrings:

        currentStringLength = len(string)
        currentStringIndex = selectedStrings.index(string)
        currentStringNumberFormat = "{:0>2} ".format(currentStringIndex + 1)
        padding = (longestStringLength - currentStringLength + 2) * " "

        if currentStringIndex % stringsPerLine == 0:
            outputString += "\n"

        outputString += currentStringNumberFormat + string + padding

    outputString += "\n"

    return outputString


if __name__ == "__main__":
    OUTPUT = string_picker(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    print(OUTPUT)
