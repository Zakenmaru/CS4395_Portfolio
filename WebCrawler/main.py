# Names: Shreya Valaboju, Soham Mukherjee
# Course/Section: CS 4395.001
# Portfolio 6: Web Crawler
# To-Do:
#   - need to get some links outside of domain and extract text
#   - currently, it's just extracting info about players on the team
#   - need to build knowledge base

# import libraries
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import os
import re
import sys
import pickle
import math
import nltk
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
nltk.download('punkt')


#Build a searchable knowledge base of facts that a chatbot (to be developed later) can
#share related to the 10 terms. The “knowledge base” can be as simple as a Python dict
#which you can pickle. More points for something more sophisticated like sql.
def knowledgeBase():
    return 0





# calculates terrm frequencies of all documents
def tf(text):

    tf_dict={}
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w.isalpha() and w not in stopwords]  #extract alpha and non-stopwords only

    # get term frequencies in a more Pythonic way
    token_set = set(tokens)
    tf_dict = {t: tokens.count(t) for t in token_set}

    # normalize tf by number of tokens
    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(tokens)

    return tf_dict


#Write a function to extract at least 25 important terms from the pages using an
#importance measure such as term frequency, or tf-idf.
#First, it’s a good idea to lowercase everything, remove stopwords and punctuation. Print the top 25-40 terms.
# create tf-idf dictionaries for each file
def create_tfidf(tf,idf):
    tf_idf = {}
    for t in tf.keys():
        tf_idf[t] = tf[t] * idf[t]
    return tf_idf


def tfidf(sentence_files):

    vocab_per_url =[]
    tf_dicts_all = []
    vocab = set()

    for sf in sentence_files:
        current_file = open(sf, "r", encoding="utf-8")  # open file to read

        # lowercase, remove punctuation
        text = current_file.read().lower()
        text = re.sub(r'[^\w\s]', '', text)

        # get tf (term frequencies) dictionaries for each file
        tf_dict= tf(text)
        vocab_per_url.append(tf_dict.keys())
        tf_dicts_all.append(tf_dict)

        # add to vocab
        vocab = vocab.union(set(tf_dict.keys()))


    # get idf
    idf_dict={}
    for term in vocab:
        temp = ['x' for voc in vocab_per_url if term in voc]
        idf_dict[term] = math.log((1 + len(sentence_files)) / (1 + len(temp)))

    # get tf-idf dictionary for each document and print top 25 terms from each
    tf_idf = {}
    url_num=0
    for termf in tf_dicts_all:
        tfd = create_tfidf(termf,idf_dict)
        doc_term_weights = sorted(tfd.items(), key=lambda x: x[1], reverse=True)
        print("\nPlayer "+ str(url_num)+ " top 25 terms: ", doc_term_weights[:25])
        url_num+=1





#Write a function to clean up the text from each file. You might need to delete newlines
#and tabs first. Extract sentences with NLTK’s sentence tokenizer. Write the sentences for
# each file to a new file. That is, if you have 15 files in, you have 15 files out.
def clean(files_arr):

    sentences_files=[]

    for f in files_arr:
        current_file = open(f, "r", encoding="utf-8")  # open file to read
        text_in = current_file.read()

        # remove newlines, tabs
        text_in = text_in.strip()
        text_in = re.sub('\s+', ' ', text_in)

        # lowercase, everything between brackets, parenthesis
        text_in = re.sub("\(.*?\)","",text_in)
        text_in = re.sub("\[.*?\]", "", text_in)


        # extract sentences using nltk's tokenizer, write sentences to a new file
        sent_arr= sent_tokenize(text_in)
        fname= "cleaned_"+f
        cleaned_file = open(fname,'a', encoding="utf-8")
        for sentence in sent_arr:
            cleaned_file.write(sentence +"\n")
        sentences_files.append(fname)
        cleaned_file.close()

    # call to tf-idf function
    tfidf(sentences_files)


def accessPage(base_url):

    urls=[]
    files=[]

    base_page = requests.get(base_url)
    base_soup = BeautifulSoup(base_page.content, 'html.parser')

    #for p in base_soup.select('p'):
    #    print(p.get_text())

    #tables = base_soup.find_all('table')
    #for child in base_soup.find_all('table')[0].children:
    #    for td in child:
    #        print(td.text)

    # get players links (15)
    name_column_number=0
    table = base_soup.find('table', class_='sortable')  # the table with information about each player
    #table = base_soup.find_all('table')[0] - for link 7
    for row in table.tbody.find_all('tr'):  # iterate through each row of the table
        name_column_number = 0
        columns = row.find_all('td') # get the columns of the table
        for td in columns:
            if td.a and name_column_number ==2: # the second column holds the name of each player hyperlinked to their own wiki pages
                urls.append(urljoin(base_url, td.a.get('href')))
                #print(urljoin(base_url, td.a.get('href')))
            name_column_number+=1

    # get external links (5) from reference list
    #x=0
    #reference_data = base_soup.findAll('div', attrs={'class': 'reflist'})
    #for div in reference_data:
    #    links = div.findAll('a')
    #    for a in links:
    #        if x == 10:
    #            break
    #        link_str = urljoin(base_url,a.get('href'))
    #        if 'wiki' not in link_str:
    #            urls.append(urljoin(base_url, link_str))
    #            print(urljoin(base_url, link_str))
    #            x+=1


    # Write a function to loop through your URLs and scrape all text off each page. Store each page’s text in its own file
    for i in range(len(urls)):
        # create new soup objects and request for each link we scrape from
        page = requests.get(urls[i])
        soup = BeautifulSoup(page.content, 'html.parser')
        file_name = 'url'+str(i)+'.txt' # name of the file to be created
        files.append(file_name)
        for p in soup.select('p'):
            url_file = open(file_name, "a", encoding="utf-8")  # file with the predicted languages for each line in the test file
            url_file.write(p.get_text() + '\n')
            #print(p.get_text())

    clean(files)

if __name__ == '__main__':
    # https://www.mavs.com/team/roster/
    # https://www.nba.com/player/1629029/luka-doncic/profile
    # https://en.wikipedia.org/wiki/Template:Dallas_Mavericks_roster
    # https://en.wikipedia.org/wiki/Dallas_Mavericks
    # https://en.wikipedia.org/wiki/Dallas_Mavericks_all-time_roster_and_statistics_leaders
    # https://www.nba.com/team/1610612742/mavericks
    # https://en.wikipedia.org/wiki/Luka_Don%C4%8Di%C4%87 (7)
    url = 'https://en.wikipedia.org/wiki/Dallas_Mavericks'

    # Remove all url files at the start
    for i in range(34):
        file_name = 'url' + str(i) + '.txt'
        file_name2 = 'cleaned_url' + str(i) + '.txt'
        if os.path.exists(file_name):
            os.remove(file_name)
        if os.path.exists(file_name2):
            os.remove(file_name2)

    accessPage(url)


