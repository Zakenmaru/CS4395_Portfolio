
# Name: Shreya Valaboju, sxv180047
# Name: Soham Mukherjee, sxm180113
# Course/Section: CS 4395.001
# Program 1, Portfolio 4: Ngrams
# Notes:
#   - RUN THIS FILE BEFORE RUNNING PROGRAM 2
#   - THIS FILE IS EXECUTED 3 TIMES, ONCE FOR EACH LANGUAGE. THE SYSARGV[1] FOR THIS SHOULD BE ONE OF THE 3 LANGUAGE'S TRAINING DATA,
#       FOR EXAMPLE, 'LangId.train.English'.
#   -  AFTER RUNNING 3 TIMES, YOU SHOULD END UP WITH 6 PICKLE FILES. EACH LANGUAGE SHOULD HAVE 1 CONTAINING THE BIGRAM DICTIONARY AND ANOTHER WITH THE UNIGRAM DICTIONARY.


# import necessary libraries
import sys
import pathlib
import re
import pickle
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
nltk.download('punkt')



# use the bigram list to create a bigram dictionary of bigrams and counts, [‘token1 token2’] -> count
def createBigramDictionary(bigrams):
    #bigrams_dict = {b: bigrams.count(b) for b in set(bigrams)}
    bigrams_dict={}
    print("Creating Bigrams Dictionary...")
    for b in set(bigrams):
        bigrams_dict[b]=bigrams.count(b)
    return bigrams_dict


# generate unigrams using nltk's ngrams(), generator
def generateUnigrams(unigrams):
    print("Creating Unigram Dictionary...")
    unigram_dict = {t:unigrams.count(t) for t in set(unigrams)}
    return unigram_dict


# generate bigrams using nltk's ngrams()
def generateBigrams(tokens):
    bigrams = list(ngrams(tokens, 2))
    return bigrams


# tokenize and perform basic preprocessing (check if this is necessary)
def tokenize(text):
    text = text.lower()
    tokens_arr = word_tokenize(text)
    tokens = [t for t in tokens_arr if t.isalpha()] #only count alphabetical tokens, no numbers or punctuation
    return tokens






def start(text_in):
    tokens = tokenize(text_in)  # start program

    # create a bigram dictionary of counts
    bigrams_list = generateBigrams(tokens)
    bigrams_dict = createBigramDictionary(bigrams_list)
    print(bigrams_dict)

    # create a unigram dictionary of counts
    unigram_dict = generateUnigrams(tokens)
    print(unigram_dict)

    return unigram_dict,bigrams_dict

# pickle the unigram and bigram dictionaries
def pickleDictionaries(uni_dict, bi_dict, lang):
    pickle.dump(uni_dict, open(lang + '_train_unigram.p', 'wb'))
    pickle.dump(bi_dict, open(lang + '_train_bigram.p', 'wb'))




if __name__ == '__main__':
    if len(sys.argv) < 2:  # check if number of arguments is at least 1, if not terminate program
        print("ERROR: Please enter argument (sysarg) containing input/data file relative path. Re-run program.")
        quit()

    try:
        file_path = pathlib.Path.cwd().joinpath(sys.argv[1])
        lang = str(file_path).split("train.")[1].lower()
        with open(file_path,  'r', encoding="utf8") as f:  # find data file and open
            text_in = f.read()
            unigram_dict, bigram_dict = start(text_in)

            
            # pickle unigram and bigram dictionaries into files
            pickleDictionaries(unigram_dict,bigram_dict, lang)
    except FileNotFoundError:
        print("ERROR: Input/data file provided cannot be found. Please re-run program.")
        quit()