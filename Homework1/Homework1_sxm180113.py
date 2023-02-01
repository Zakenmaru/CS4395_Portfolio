"""
Soham Mukherjee
sxm180113
CS 4395 - Professor Mazidi
1/30/2022
"""
import os.path
import sys


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


def run_program():
    filename = check_args()


if __name__ == '__main__':
    run_program()
