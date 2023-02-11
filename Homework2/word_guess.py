import sys
import os
import nltk

nltk.download('punkt')
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('averaged_perceptron_tagger')

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess(filename):
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    with open(filename, 'r') as f:
        text = f.read()
    # convert text to lowercase
    text = text.lower()
    # tokenize the lowercase text
    tokens = nltk.word_tokenize(text)
    # edit the tokens to reduce them to those that are alpha, not in stopword list, and have length > 5
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words and len(token) > 5]

    # lemmatize tokens
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # get unique lemmas and do Part-of-Speech(pos) tagging.
    unique_lemmas = set(tokens)
    tagged = nltk.pos_tag(unique_lemmas)
    print(tagged[:20])

    # get a list of lemmas that are nouns
    nouns = [noun for noun, tag in unique_lemmas if tag.startswith('N')]

    # print number of tokens, number of nouns
    print("Tokens: ", len(tokens))
    print("Nouns: ", len(nouns))

    # TODO: Return tokens and nouns
    return [], []


def calculate_diversity(filename):
    # open file, begin reading line by line's word contents
    words = []
    with open(filename, 'r') as f:
        for line in f:
            lst = nltk.word_tokenize(line)
            words.extend(lst)
    lex_diversity = len(set(words)) / len(words)
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
    tokens, nouns = preprocess(filename)


if __name__ == '__main__':
    run_program()
