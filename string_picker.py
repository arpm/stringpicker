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


def string_picker(inputFile, numberOfStrings, stringsPerLine):
    """Returns the randomly selected strings as a formatted string"""

    inputList = file_to_list(inputFile)

    selectedStrings = random.sample(inputList, numberOfStrings)
    longestStringLength = longest_string_length(selectedStrings)
    numberOfDigits = len(str(numberOfStrings))

    outputString = ""

    for index, string in enumerate(selectedStrings):

        currentStringLength = len(string)
        currentStringNumber = "{:0>{width}} ".format(index + 1,
                                                     width=numberOfDigits)
        padding = (longestStringLength - currentStringLength + 2) * " "

        if index % stringsPerLine == 0:
            outputString += "\n"

        outputString += currentStringNumber + string + padding

    outputString += "\n"

    return outputString


if __name__ == "__main__":
    OUTPUT = string_picker(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
    print(OUTPUT)
