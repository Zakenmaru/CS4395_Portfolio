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


def process_id(id, personnel):
    # if id is valid, then just return it; if the first 2 characters are alphabet, the last 4 are numbers,
    # and it isn't already in the dictionary then it's a valid id.
    if id[:2].isalpha() and id[2:].isdigit() and len(id) == 6 and not personnel.get(id):
        return id
    # otherwise, keep looping until a valid id is provided.
    while True:
        print("ID invalid: ", id)
        print("ID is two letters followed by 4 digits")
        id = input("Please enter a valid id: ")
        if id[:2].isalpha() and id[2:].isdigit() and len(id) == 6 and not personnel.get(id):
            break
    return id


def process_name(fields):
    last, first, middle = fields[0], fields[1], fields[2]
    # convert all 3 to Capital Case.
    last = last.capitalize()
    first = first.capitalize()
    if not middle:
        middle = "X"
    middle = middle.capitalize()
    return last, first, middle


def process(filename):
    personnel = defaultdict()
    with open(filename) as f:
        # skip the first row.
        next(f)
        for line in f:
            # unpack each line.
            fields = line.split(',')
            # extract last name, firstname , and middle initial respectively.
            last, first, middle = process_name(line[:3])
            id = process_id(line[3], personnel)


def run_program():
    filename = check_args()
    process(filename)


if __name__ == '__main__':
    run_program()
