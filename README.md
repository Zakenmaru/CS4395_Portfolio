# CS4395_Portfolio
This portfolio was created for my CS 4395 class - Human Language Technologies.

## Component 0
A paper I wrote on NLP. Check it out [here](Overview_of_NLP.pdf)!

## Component 1 - Processing Data
Program: [Code](Homework1/process.py)
### What it does
This program, given an input file of personnel, will process the given data and then print out each Person. Each Person has the following fields: **:last, first, mi, id, and phone**. This program will first check if the user-provided input is valid, then process the text itself so it can return a `Dictionary` full of `Person` objects, and finally pickle the appropriate input before outputting each `Person`.
### How to Run
In order to use this program, run it on the command line like so:
`python process.py data/data.csv`. Make sure you are within the `Homework1` folder.
### Pros and Cons of Python for Text Processing
One of the big pros of Python is that it's very easy to write readable code; this holds true for processing, and makes it very easy for other people to understand the code. Moreover, there are multiple ways to process text thanks to Python's expansive libraries and functions - apart from regex, string manipulation, NLTK, and SpaCy are also viable alternatives for text processing.
However, it also has a big con when it comes to performance. Python is slow when it comes to processing large datasets, and can sometimes be power intensive as well as a result of it. Therefore, it's very important to be mindful of using Python at scale, as it probably isn't as suited for the purpose as a lower level language.
### What I learnt
I learnt more about RegEx. Initially I was going to do string manipulation, but RegEx, while looking confusing at first, is incredibly versatile for a lot of string cases. I think I should read more into RegEx, as it's a very interesting tool to quickly match search patterns. I also learnt about pickling and its importance to binarily translate given data. It's also smaller in size due to bytes being the smallest pieces of data that can be saved. 
