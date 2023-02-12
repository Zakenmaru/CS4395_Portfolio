import random
import sys
import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from random import seed
from random import randint
seed(1234)

nltk.download('punkt')
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('averaged_perceptron_tagger')

def guessing_game(words):
    # start guessing game
    print("Let's play a word guessing game!")

    # initialize beginning points and done.
    points = 5
    done = False

    # points flag makes sure that a valid amount of points are there to play.
    # done ensures that the player hasn't quit yet.
    while not done:
        # choose a random word
        rand_i = random.randint(0, len(words) - 1)
        word = words[rand_i]

        # initialize valid letters for the given word, and blanks
        valid_letters = set(word)
        blanks = ["_"] * len(word)
        while True:
            # if no more points, game over.
            if points < 0:
                print("Game over.")
                done = True
                break
            # if the list is populated with anything other than underscores, then the word has been correctly guessed.
            solved = True
            for c in blanks:
                if c == "_":
                    solved = False
                    break
            if solved:
                print("You solved it!")
                print("\nCurrent Score: ", points)
                print("Guess another word")
                break
            print(" ".join(blanks))
            c = input("Guess a letter: ")
            if c == "!":
                done = True
                break
            if c not in valid_letters:
                points -= 1
                print("Sorry, guess again. Score is ", points)
            else:
                points += 1
                blanks = [c if word[i] == c else blanks[i] for i in range(len(word))]
                print("Right! Score is, ", points)
    print("Thanks for playing!")






def get_words(tokens, nouns):
    # make a frequency counter, then populate the count of nouns
    counter_t = Counter(tokens)
    counter_n = dict()
    for noun in nouns:
        counter_n[noun] = counter_t[noun]
    # sort the nouns based on their frequency
    sorted_nouns = sorted(counter_n.items(), key=lambda x: x[1], reverse=True)
    # retrieve the top 50 frequent nouns and return them; strip the frequency
    top_50 = sorted_nouns[:50]
    top_50 = [noun for noun, freq in top_50]
    return top_50


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
    nouns = [noun for noun, tag in tagged if tag.startswith('N')]

    # print number of tokens, number of nouns
    print("Tokens: ", len(tokens))
    print("Nouns: ", len(nouns))

    # Return tokens and nouns
    return tokens, nouns


def calculate_diversity(filename):
    # open file, begin reading line by line's word contents
    words = []
    with open(filename, 'r') as f:
        for line in f:
            lst = nltk.word_tokenize(line)
            words.extend(lst)
    lex_diversity = len(set(words)) / len(words)
    lex_diversity = round(lex_diversity, 2)
    print("Lexical Diversity: ", lex_diversity)


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
    calculate_diversity(filename)
    # get tokens and nouns
    tokens, nouns = preprocess(filename)
    # get most common words
    guessing_words = get_words(tokens, nouns)
    # play the guessing game
    guessing_game(guessing_words)


if __name__ == '__main__':
    run_program()
