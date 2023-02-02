"""
Soham Mukherjee
sxm180113
CS 4395 - Professor Mazidi
1/30/2022
"""
import os.path
import sys
import re
import pickle


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
    pattern_id = r"^[A-Za-z]{2}\d{4}$"
    # if the id isn't valid, keep looping until a valid id is provided.
    while not (re.match(pattern_id, id) and not personnel.get(id)):
        print("ID invalid: ", id)
        print("ID is two letters followed by 4 digits")
        id = input("Please enter a valid id: ")
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


def process_phone(number):
    pattern_phone = r"\w{3}-\w{3}-\w{4}"
    while not re.search(pattern_phone, number):
        print("Phone ", number, " is invalid")
        print("Enter phone number in form 123-456-7890")
        number = input("Enter phone number: ")
    return number


def process(filename):
    personnel = dict()
    with open(filename) as f:
        # skip the first row.
        next(f)
        for line in f:
            # unpack each line.
            fields = line.split(',')
            # extract last name, firstname , and middle initial respectively.
            last, first, middle = process_name(fields[:3])
            # extract id and fix if necessary.
            id = process_id(fields[3], personnel)
            # extract phone and fix if necessary.
            phone = process_phone(fields[4])
            # add new Person object to personnel.
            personnel[id] = Person(last, first, middle, id, phone)
    return personnel


def pickle_file(personnel):
    # pickle the dict
    pickle.dump(personnel, open('personnel.p', 'wb'))
    # unpickle
    personnel_pickle = pickle.load(open('personnel.p', 'rb'))
    for personnel in personnel_pickle:
        personnel_pickle[personnel].display()


def run_program():
    filename = check_args()
    personnel = process(filename)
    pickle_file(personnel)


if __name__ == '__main__':
    run_program()
