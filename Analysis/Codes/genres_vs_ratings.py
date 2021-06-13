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
from nltk.corpus import stopwords

books = pd.read_csv('./Datasets/book_data.csv',error_bad_lines = False)
#error_bad_lines : boolean, default True Lines with too many fields (e.g. a csv line with too many commas) will by default cause an exception to be raised, and no DataFrame will be returned. If False, then these “bad lines” will dropped from the DataFrame that is returned. (Only valid with C parser
print("There are {} rows and {} columns in the dataset.".format(books.shape[0], books.shape[1]))
#books.shape #table dimensions
#columns
np.array(books.columns)
#columns which contain null values and the number of null elements
null_counts = books.isnull().sum()
null_counts[null_counts > 0].sort_values(ascending=False) #null_counts in each column (sorted)
#removing stopwords from the book description #future: use the initial form of words

g= []
for i in range(books.shape[0]):
    if isinstance(books['genres'].iloc[i], str) and len(books['genres'].iloc[i])>0:
        g.append(books['genres'].iloc[i])

#figuring out all the existing genres and saving the genres in Genres_list list
Genres_dict = {}
for i in range(len(books)):
    row = books.iloc[i]
    Gen = str(row.genres)
    genres = Gen.split('|')
    for genre in genres:
        if genre not in Genres_dict:
            Genres_dict[str(genre)] = []
            Genres_dict[str(genre)].append(books.iloc[i]['book_rating'])
        else:
            Genres_dict[str(genre)].append(books.iloc[i]['book_rating'])
#len(Genres_list)

#figuring out all the existing genres and saving the genres in Genres_list list
Genres_dict_count = {}
for i in range(len(books)):
    row = books.iloc[i]
    Gen = str(row.genres)
    genres = Gen.split('|')
    for genre in genres:
        if genre not in Genres_dict_count:
            Genres_dict_count[str(genre)] = 1
        else:
            Genres_dict_count[str(genre)] +=1
#len(Genres_list)

genres_average_rating = {}
for k, v in Genres_dict.items():
    if k not in genres_average_rating:
        genres_average_rating[k] = np.mean(v)

#also can be derived from our function in part wc_genres.py
most_frequent_gens ={'Contemporary': 6039,
 'Classics': 6272,
 'Historical Fiction': 6399,
 'Science Fiction': 6780,
 'Nonfiction': 7598,
 'Mystery': 7902,
 'Paranormal': 7994,
 'Historical': 10789,
 'Young Adult': 11251,
 'Romance': 18636,
 'Fantasy': 23583,
 'Fiction': 25736}

frequent_gs = list(most_frequent_gens.keys())
frequent_counts = list(most_frequent_gens.values())
frequent_rates = [genres_average_rating[i] for i in frequent_gs]

#### import random
number_of_colors =len(frequent_gs) #len
r = ["#"+''.join([random.choice('0123456789ABCDFE') for j in range(6)])
             for i in range(number_of_colors)]
random_colors = ["Crimson", "pink", "#FFFF00", "#663399","Orange", "#90EE90", "#808000",
                "#1E90FF", "#0000FF", "#DAA520", "#228B22", "red", "#3CB371"]
plt.figure(figsize=(12, 9))
for i in range(len(frequent_counts)):
    plt.scatter(frequent_counts[i],frequent_rates[i],
                      c=random_colors[i],
                     alpha=0.5,
               s = frequent_counts[i], label=frequent_gs[i])
for i, j in zip(frequent_counts, frequent_rates):
    plt.text(i-300, j, s=str(np.round(j, 2)), c="navy", size=10)

plt.rcParams["legend.markerscale"] = 0.1
plt.legend(markerscale=0.07,bbox_to_anchor=(1, 1), loc='upper left', ncol=1)
plt.xlabel("Frequency of genres", size=14)
plt.ylabel("Average rating", size=14)
plt.title("Most frequent genres average ratings vs frequency", size=16)
plt.savefig("freq_genres_ratings_2.png")
