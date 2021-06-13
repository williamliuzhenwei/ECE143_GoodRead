import pandas as pd #for importing csv file
import numpy as np #for sum mathematical stuff
import matplotlib.pyplot as plt #for plotting
import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
import re
import time
import string
import collections
from collections import Counter
from wordcloud import WordCloud
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import ShuffleSplit
import sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import collections
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def clean_words (string_g):
    """
    given a string, removes stopwords, non-english words, punctuations
    """
    #fiction_string = ' '.join([word for word in fiction_string.split() if word not in stopwords_dict])
    #fiction_string = ' '.join([word for word in fiction_string.split() if isEnglish(word)])
    assert isinstance(string_g, str)
    string_g = "".join(l for l in string_g if l not in string.punctuation) #remove punctuation
    string_words = string_g.split()
    string_words = [string_words[i].lower() for i in range(len(string_words))] #lower
    #fiction_words = [fiction_words[i] if fiction_words[i] not in stopwords_dict] #not stop words
    words = []
    for i in range(len(string_words)): #english
        if string_words[i] not in stopwords_dict:
            if isEnglish(string_words[i]):
                if string_words[i] not in stop_words:
                    words.append(string_words[i])
                else:
                    pass
    word_freq = {}
    for i in words:
        if i not in word_freq and len(i)>2:
            word_freq[i] = 1
        elif len(i)>2 and i in word_freq:
            word_freq[i] +=1
    return word_freq


#returning most frequent words of a dictionary
def most_freq_in_dictionary(diction, top):
    """
    returning most frequent words of a dictionary
    """
    assert isinstance(diction, dict)
    assert isinstance(top, int)
    assert top > 0
    sorted_diction = {k: v for k, v in sorted(diction.items(), key=lambda item: item[1])}
    values = sorted(sorted_diction.values())
    wc = {}
    for k,v in sorted_diction.items():
        if v in values[-top:]:
            wc[k] = v
    #value, count = collections.Counter(diction.values()).most_common(top)
    return sorted_diction, values[-top:], wc



#function for removing non-english words
def isEnglish(s):
    """
    checks whether s is a string or not
    """
    assert isinstance(s, str)
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
assert not isEnglish('کتاب')

def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40,
        scale=10,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title:
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()


def plot_wc(diction, filename):
    """
    given a dictionary plots its wc
    """
    assert isinstance(diction, dict)
    assert isinstance(filename, str)
    #word_could_dict=Counter(g)
    custom_mask = np.array(Image.open("book.png"))
    wordcloud = WordCloud(background_color="white",
                          #mode="RGBA",
                          #colormap='Dark2',
                          #colormap='RdBu',
                          colormap='BrBG',
                          collocations=False,
                          mask=custom_mask, contour_width=1,
                          contour_color='black',
                         width=1200, height=1000,
                          max_font_size=80,
                          scale=3,
                         ).generate_from_frequencies(diction)
    #wc = WordCloud(background_color="white", mask=custom_mask)
    #wc = WordCloud(background_color="white", collocations=False, mask=custom_mask, contour_width=1, contour_color='gray')
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig("{}.png".format(filename))
    plt.show()
#source: https://medium.com/swlh/masking-with-wordcloud-in-python-500-most-frequently-used-words-in-german-c0e865e911bb


books = pd.read_csv('book_data.csv',error_bad_lines = False)
#error_bad_lines : boolean, default True Lines with too many fields (e.g. a csv line with too many commas) will by default cause an exception to be raised, and no DataFrame will be returned. If False, then these “bad lines” will dropped from the DataFrame that is returned. (Only valid with C parser
print("There are {} rows and {} columns in the dataset.".format(books.shape[0], books.shape[1]))
#books.shape #table dimensions
#columns
np.array(books.columns)
#columns which contain null values and the number of null elements
null_counts = books.isnull().sum()
null_counts[null_counts > 0].sort_values(ascending=False) #null_counts in each column (sorted)
#removing stopwords from the book description #future: use the initial form of words
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
#stop_words
#books[['book_title', 'genres']]
desired_genres = ['Fiction', 'Classics', 'Sports', 'Romance'] #from another analysis in the following

#books = books[books['book_title'].notna()] #removing nulls in book_title column
books = books[books['genres'].notna()] #removing nulls in genres column


s = time.time()
fiction_string = ""
classics_string = ""
sports_string = ""
romance_string = ""
for i in range(len(books)):
    genre = books['genres'].iloc[i]
    title = books['book_title'].iloc[i]
    if desired_genres[0] in genre:
        fiction_string+= str(title) + " "
    if desired_genres[1] in genre:
        classics_string+= str(title) + " "
    if desired_genres[2] in genre:
        sports_string+= str(title) + " "
    if desired_genres[3] in genre:
        romance_string+= str(title) + " "
print("Took {} seconds".format(time.time() -s ))
#fiction_string[:100]

stopwords_dict = Counter(stop_words)

word_freq = clean_words(fiction_string)
d_fiction, v_fiction, wc_fiction = most_freq_in_dictionary(word_freq, 50)

word_freq = clean_words(classics_string)
d_classics, v_classics, wc_classics = most_freq_in_dictionary(word_freq, 50)

word_freq = clean_words(sports_string)
d_sports, v_sports, wc_sports = most_freq_in_dictionary(word_freq, 50)

word_freq = clean_words(romance_string)
d_romance, v_romance, wc_romance = most_freq_in_dictionary(word_freq, 50)


stopwords = set(STOPWORDS)

#---------------run ----------------
plot_wc(wc_sports, "sport_wc")
plot_wc(wc_fiction, "fiction_wc")
plot_wc(wc_romance, "romance_wc")
