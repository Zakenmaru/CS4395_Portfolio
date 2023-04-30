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
## Component 2 - Guessing Game
Program: [Code](Homework2/word_guess.py)
### What it does
This program will preprocess text data from an anatomy textbook and play a guessing game with the user, using the 50 most common words from the data as potential words. The user must then input the correct letters to solve the word. Correct guesses lead to an increase in points, whereas incorrect guesses lead to a decrease in points. If the player types in an "!" or they get less than 0 points, then the game terminates. 
### How to Run
In order to use this program, run it on the command line like so:
`python word_guess.py anat19.txt`. Make sure you are within the `Homework2` folder.
## Component 3 - WordNet
Program: [Code](Homework3/WordNetNotebook.pdf)
### What it does
This program runs through the different uses of WordNet, including origins of word, finding sentiment from words, as well as collocations. It runs through different tasks to do so.
### How to Run
Download the notebook and run it within your notebook environment. Make sure to download the necessary resources.
## Component 4 - Ngrams
### Name: Shreya Valaboju, sxv180047
### Name: Soham Mukherjee, sxm180113
Program 1: [Code](Homework4/program1.py)
Program 2: [Code](Homework4/program2.py)
Narrative: [Link](Homework4/portfolio4_cs4395.001_narrative.pdf)
### What it does
This program will train given input data in English, French, and Italian and try to identify sentences using testing data. The outputs will be the accuracy (number of sentences correctly classified), as well as the line numbers which were incorrect. As of writing this, the accuracy should be ~95%. 

### How to Run
#### Program 1
Given appropriate training data, Program 1 will make unigrams/bigrams out of the data and store them in pickle files. The following files are available:
- **data/LangId.train.English**
- **data/LangId.train.French**
- **data/LangId.train.Italian**

In order to run the program, run it as such: 

`python program1.py  python program1.py data/LangID.train.English data/LangID.train.French data/LangID.train.Italian`

#### Program 2
After the unigrams and bigrams are created, it's time to test them using sample data. Run the following command: 

`python program2.py data/LandId.test data/LandId.sol`
## Component 5 - Sentence Parsing
Document: [Link](sxm180113_sentenceparse.pdf)

## Web Crawler
Report: [Link](WebCrawler/web_crawler_report.pdf)
Program: [Code](WebCrawler/main.py)
### How to Run
Run the file as-is. It'll create the knowledge base of players and store them within a Pickle file.

## Text Classification
PDF: [Code](TextClassification/sxm180113_text_classification.pdf)

## ACL Paper
PDF: [Paper](sxv180047_sxm180113_summary_acl_paper_cs4395.001.pdf)

## Chatbot
Code: [NBA-Chatbot](NBA-Chatbot/chatbot.py)

## Text Classification 2
PDF: [Code](TextClassification/sxm180113_text_classification_2.pdf)

# Summary

### NLP Skills
Throughout the course, I refined my skills in preprocessing, as well as learning new ones in making NLP models. Whether it was techniques like TF-IDF, using RNNs, or more, I thoroughly enjoyed my time in this class learning more about the joy of Natural Language Processing. The projects were very, very fun, and forced me to think more about _why_ I was doing the project rather than _what_. I also learnt a lot more about the Mavericks.

### Why NLP?
I honestly chose this class at first on recommendation of a friend, without really knowing what NLP was about. Honestly, I thought it was identifying handwritten numbers (before I realized that was Computer Vision). I quickly grew to enjoy it as it taught me the joy of linguistics on both a semantic and technical level. It made a lot of sense despite being a confusing subject from the outside. I got to learn more not only about the technology and libraries behind it, but also human interactions as a whole. I can see why it's called Human Language Technologies instead of Natural Language Processing - it is quite literally, the study of how humans interface their language to technology.

### Future Personal Project
I like writing a book series in my freetime, but I also like programming. At the intersection of these two, I want to create a comprehensive writing Discord bot which readers and users alike can query for information about the book, such as characters, settings, plot, etc. 

Currently, in my writing Discord, I have an MVP of the bot which users can query about characters and general information using preset Discord commands. I want to expand this using the techniques I learnt in class to make a fully-functioning, NLP-based version of the bot. Ideally, it will dynamically respond to users' queries without needing to parse a specific command. 

### Keeping Up With The NLPians
With the advent of big data, machine learning, artificial intelligence, digital manufacturing, big data analysis, quantum communication and internet of things, Natural Language Processing is a hotter topic more than ever. I already use Medium and TechCrunch to keep up with 

### Future Opportunities
I would like to get opportunities, especially in this uncertain economic climate. I'm primarily seeking software engineering roles, and I have a fundamental understanding of Natural Language Processing due to having taken coursework on the subject. I would like to work on the systems that handle such large batches of data and processing, as I feel it would be really fun.

### Conclusion to the Conclusion
All in all, I really enjoyed my time with this class, and I look forward to taking the skills, both hard and soft, to the next step!

