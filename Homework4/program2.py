# Name: Shreya Valaboju, sxv180047
# Course/Section: CS 4395.001
# Program 2, Portfolio 4: Ngrams
# Notes:
#   - RUN PROGRAM 1 FIRST. PROGRAM 1 CREATES 6 PICKLE FILES WHICH ARE NEEDED IN THIS PROGRAM
#   - AFTER EACH RUN, DELETE ALL THE CONTENTS FROM THE 'RESULTS.TXT' FILE, SINCE WE APPEND TO IT EACH RUN (SEE NOTES BELOW)
#   - the probabilities are really small, but they are not 0. The classifications are correct tho, just make sure i'm doing this right








#  import necessary libraries
import sys
import pathlib
import re
import pickle
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
nltk.download('punkt')

# c. Compute and output your accuracy as the percentage of correctly classified instances in the
#       test set. The file LangId.sol holds the correct classifications.
# d. output your accuracy, as well as the line numbers of the incorrectly classified items
def compute_accuracy(f):

    accuracy = 0
    total=0 # total number of classifications made
    incorrect_lines =[] # holds the line numbers of the incorrectly classified lines

    results_file = open("result.txt", "r")
    correct_file = open(f,"r")

    results = results_file.readlines()
    correct = correct_file.readlines()

    for l in range(len(results)):
        if results[l] == correct[l]:   # correctly classified language
            accuracy += 1
        else: # incorrectly classified, save line numbers into array
            incorrect_lines.append(correct[l].split(" ")[0])

        total+=1


    accuracy = accuracy/total # compute accuracy as number of correctly classified lines/total classifications made
    print("Accuracy: ", str(accuracy))
    print("Incorrect Classification Line Numbers: ", incorrect_lines)





# b. For each line in the test file, calculate a probability for each language (see note below) and
#       write the language with the highest probability to a file.
#  Each bigram’s probability with Laplace smoothing is: (b + 1) / (u + v) where b is the bigram count,
#       u is the unigram count of the first word in the bigram, and v is the total vocabulary
#       size (add the lengths of the 3 unigram dictionaries).
def compute_prob(eb,eu,ib,iu,fb,fu, test_data):

    # 'eu' : english unigram dictionary
    # 'eb' : english bigram dictionary
    # 'iu' : italian unigram dictionary
    # 'ib' : italian bigram dictionary
    # 'fu' : french unigram dictionary
    # 'fb' : french bigram dictionary


    v= len(eu) + len(iu) + len(fu)  # v is the total vocabulary size (add the lengths of the 3 unigram dictionaries).
    lineNum=1

    # read test data line by line
    for test in test_data.splitlines():

        # 1. create bigrams, unigrams for test line
        unigrams_test = word_tokenize(test)
        bigrams_test = list(ngrams(unigrams_test, 2))
        print(test) # print the test line

        #2. calculate the probability using laplace smoothing for each language-  english, italian, french (refer to prof's notebook)
        p_laplace_english = 1
        for bigram in bigrams_test:
            b = eb[bigram] if bigram in eb else 0
            u = eu[bigram[0]] if bigram[0] in eu else 0
            p_laplace_english = p_laplace_english * ((b + 1) / (u + v))

        print("Probability (English): %.10f" % p_laplace_english)

        ###########################################################################
        p_laplace_italian = 1
        for bigram in bigrams_test:
            b = ib[bigram] if bigram in ib else 0
            u = iu[bigram[0]] if bigram[0] in iu else 0
            p_laplace_italian = p_laplace_italian * ((b + 1) / (u + v))

        print("Probability (Italian): %.10f" % p_laplace_italian)

        ###########################################################################
        p_laplace_french = 1
        for bigram in bigrams_test:
            b = fb[bigram] if bigram in fb else 0
            u = fu[bigram[0]] if bigram[0] in fu else 0
            p_laplace_french = p_laplace_french * ((b + 1) / (u + v))

        print("Probability (French): %.10f" % p_laplace_french)
        print("\n")

        # 3. write to file which language has the highest probability, and that is the classification that's made
        # *** we APPEND to the file. make sure at each run, 'results.txt' is empty.
        result_file = open("result.txt", "a") # holds the classifications for each line, the 'results.'
        highest_probability = max(p_laplace_french,p_laplace_italian,p_laplace_english)
        if highest_probability == p_laplace_english:
            result_file.write(str(lineNum)+ " English\n")
        elif highest_probability == p_laplace_french:
            result_file.write(str(lineNum)+ " French\n")
        else:
            result_file.write(str(lineNum)+ " Italian\n")
        result_file.close()
        lineNum+=1






if __name__ == '__main__':
    if len(sys.argv) < 3:  # check if number of arguments is at least 1, if not terminate program
        print("ERROR: Please enter argument (sysarg) containing training and test files' relative paths. Re-run program.")
        quit()

    try:
        # a. Read in pickled dictionaries.
        # open pickle file, save bigrams, unigrams for all languages to dictionaries
        eb = pickle.load(open('english_train_bigram.p', 'rb'))
        eu= pickle.load(open('english_train_unigram.p', 'rb'))
        ib = pickle.load(open('italian_train_bigram.p', 'rb'))
        iu= pickle.load(open('italian_train_unigram.p', 'rb'))
        fb = pickle.load(open('french_train_bigram.p', 'rb'))
        fu = pickle.load(open('french_train_unigram.p', 'rb'))

        # SYSARGV[1] = 'LangId.test'
        # SYSARGV[2] = 'LangId.sol'

        with open(pathlib.Path.cwd().joinpath(sys.argv[1]), 'r') as f:  # find test file and open
            compute_prob(eb,eu,ib,iu,fb,fu,f.read()) #compute the probabilities using the training data from the pickle files
            compute_accuracy(sys.argv[2])

    except FileNotFoundError:
        print("ERROR: Input/data file provided cannot be found. Please re-run program.")
        quit()