import sys
import os
import nltk
nltk.download('punkt')


def calculate_diversity(filename):
    # open file, begin reading line by line's word contents
    words = []
    with open(filename, 'r') as f:
        for line in f:
            lst = nltk.word_tokenize(line)
            words.extend(lst)
    lex_diversity = len(set(words))/len(words)
    lex_diversity = round(lex_diversity, 2)
    return lex_diversity


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
    # calculate lexical diversity of the text
    lex_diversity = calculate_diversity(filename)



if __name__ == '__main__':
    run_program()