import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import csv
import seaborn as sns
import statistics as stat
import collections
from numpy.random import rand
from matplotlib.colors import ListedColormap
my_cmap = ListedColormap(sns.color_palette('YlOrBr'))
from matplotlib.colors import Normalize

def get_genres_spanned(df):
    '''
    desc: plots the distr of # of genres spanned,
    as well as the added ratings groups of books
    overlaid
    :param df: books dataframe, made from reading .csv file of data
    :type df: dataframe
    '''
    assert isinstance(df, pd.DataFrame)
    # BOOK RATINGS VS GENRES SPANNED
    # QUERY 2: Books ratings vs # genres spanned 
    # (do people like books that are about a variety of themes/topics or just a few?)
    # dict key some span of rating (ie. 4 - 4.25, 4.25 - 4.5, etc.)
    # value is # of genres they span
    books= df
    genre_span_list = np.zeros(len(books['genres']))
    for x in books['genres'].index:
        num_genres = str(books['genres'][x]).count('|') + 1
        genre_span_list[x] = num_genres

    #print(len(genre_span_list))
    #print(genre_span_list)

    genre_span_dict = {}
    for x in range(len(genre_span_list)):
        if (genre_span_list[x] not in genre_span_dict):
            genre_span_dict[genre_span_list[x]] = 1
        else:
            genre_span_dict[genre_span_list[x]] += 1

    ordered_genre_span_dict = collections.OrderedDict(sorted(genre_span_dict.items()))
    x = ordered_genre_span_dict.keys()
    y = ordered_genre_span_dict.values()
    plt.figure(figsize=(6, 4))
    plt.bar(x, y, color='salmon', edgecolor="black", width=1)
    plt.title('Distribution of Number of Genres Spanned')
    plt.xlabel('Number of Genres')
    plt.ylabel('Number of Books')
    #plt.axvline(x= ave_genres_per_book/total_num_books, color="blue", label="mean")
    #plt.legend(loc="upper left")
    plt.xticks(range(18))
    plt.xlim(1,18)
    plt.tight_layout()
    plt.savefig('genres_span_distr.png', dpi=300)

    # PLOT 2: vs OVERLAID RATING GROUPS
    books['rate_group'] = pd.cut(books['book_rating'],bins=[0,3,3.5,4,4.5,5], labels=['Poor (0-3)','Bad (3-3.5)','Decent (3.5-4)', 'Good (4-4.5)','Extremely Good (4.5-5)'])
    genre_span_arr = np.array(genre_span_list)
    books = books.sort_index(axis=0,ascending=True)
    books['genres_spanned'] = genre_span_arr
    d = books.groupby(['genres_spanned', 'rate_group'])['genres'].size().unstack()
    d.plot(kind='bar', stacked=True, title = 'Ratings of Books vs Number of Genres Spanned', colormap=my_cmap)
    plt.xlabel('Number of Genres Spanned')
    plt.ylabel('Number of Books')
    plt.tight_layout()
    plt.savefig('genre_span_rating.png', dpi=300)
    plt.show()   

#books = pd.read_csv('book_data.csv',error_bad_lines = False)
#get_genres_spanned(books)