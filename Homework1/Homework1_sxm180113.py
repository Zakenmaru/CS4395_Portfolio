"""
Soham Mukherjee
sxm180113
CS 4395 - Professor Mazidi
1/30/2022
"""
import os.path
import sys
from collections import defaultdict


class Person:
    def __init__(self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    # prints the employee id, then their name, and finally their phone #
    def display(self):
        print("Employee id:", self.id)
        print("\t\t", self.first, self.mi, self.last)
        print("\t\t", self.phone)


def check_args():
    # check if number of args is valid.
    if len(sys.argv) < 2:
        print('ERROR: Please enter a filename as a system arg! Format: \'python Homework1_sxm180113.py '
              '<filename>\'')
        sys.exit(1)
    else:
        fp = sys.argv[1]
        # check if the filename is valid or exists.
        if not os.path.isfile(fp):
            print('ERROR: Specified file not found. Please specify a proper filename!')
            sys.exit(1)
        return fp


def process(filename):
    personnel = defaultdict()
    with open(filename) as f:
        # skip the first row.
        next(f)
        for line in f:
            # unpack each line.
            fields = line.split(',')
            # extract last name, firstname , and middle initial respectively.
            last, first, middle = fields[0], fields[1], fields[2]
            last = last.capitalize()
            first = first.capitalize()
            if not middle:
                middle = "X"
            middle = middle.capitalize()



def run_program():
    filename = check_args()
    process(filename)


if __name__ == '__main__':
    run_program()
