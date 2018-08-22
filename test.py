"""This file tests the strinpicker module"""

from stringpicker import string_picker
import sys

FILE = open(sys.argv[1], 'r')

QUESTIONS = [line.rstrip() for line in FILE]

OUTPUT = string_picker(QUESTIONS, int(sys.argv[2]), int(sys.argv[3]))
print(OUTPUT)
