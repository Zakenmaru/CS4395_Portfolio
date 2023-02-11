import sys
import os


def check_args():
    # check if number of args is valid.
    if len(sys.argv) < 2:
        print('ERROR: Please enter a filename as a system arg! Format: \'python word_guess.py '
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
    # check if cmd line args are valid
    filename = check_args()


if __name__ == '__main__':
    run_program()