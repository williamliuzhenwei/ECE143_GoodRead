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

def get_correlation_matrix(df):
    '''
    desc: takes different feature columns (all numerical) including book ratings
    and plots a correlation matrix with the correlation coefficients

    :param df: books dataframe, made from reading .csv file of data
    :type df: dataframe
    '''
    assert isinstance(df, pd.DataFrame)
    # Correlation Matrix
    books = df
    # add NUMERICAL book pages column count in dataframe, for correlation matrix
    book_pages = books['book_pages'].str.rstrip('pages ')
    book_pages = book_pages.dropna()
    book_pages = book_pages.astype(int, copy=True, errors='raise')
    books['book_pgs'] = book_pages

    # add NUMERICAL book format column count in dataframe, for correlation matrix
    book_format_list = np.zeros(len(books['book_format'])) 
    paperback_count = 0
    hardcover_count = 0
    kindle_count = 0
    mmp_count = 0
    ebook_count = 0
    other_count = 0
    book_form_list = []

    for x in books['book_format'].index:
        if books['book_format'][x]== 'Paperback':
            paperback_count+=1
            book_form_list.append(1)
        elif books['book_format'][x]== 'Hardcover':
            hardcover_count+=1
            book_form_list.append(2)
        elif books['book_format'][x]== 'Kindle Edition':
            kindle_count+=1
            book_form_list.append(3)
        elif books['book_format'][x]== 'Mass Market Paperback':
            mmp_count+=1
            book_form_list.append(4)
        elif books['book_format'][x]== 'ebook':
            ebook_count+=1
            book_form_list.append(5)
        else:
            book_form_list.append(0)
            other_count+=1
    book_form_arr = np.array(book_form_list)
    books['books_format'] = book_form_arr

    # add NUMERICAL book genres spanned column count in dataframe, for correlation matrix
    genre_span_list = np.zeros(len(books['genres']))
    for x in books['genres'].index:
        num_genres = str(books['genres'][x]).count('|') + 1
    genre_span_list[x] = num_genres
    genre_span_arr = np.array(genre_span_list)
    books = books.sort_index(axis=0,ascending=True)
    books['genres_spanned'] = genre_span_arr

    # add NUMERICAL book title word length spanned column count in dataframe, for correlation matrix
    title_len_list = np.zeros(len(books['book_title']))
    for x in books['book_title'].index:
        num_title_words = int(len(str(books['book_title'][x]).split()))
        title_len_list[x] = num_title_words
    title_len_arr = np.array(title_len_list)
    books['title_word_len'] = title_len_arr

# --------------------------------------------------------------------------
    df_core = pd.concat([books['book_rating'], books['book_pgs'], books['book_rating_count'],books['book_review_count'],books['genres_spanned'], books['title_word_len'], books['books_format']], axis=1, keys=['book_rating', 'book_pages', 'rate_count', 'rev_count', 'genres_spanned', 'title_word_len','books_format'])

    corrMatrix2 = df_core.corr()
    sns.heatmap(corrMatrix2, annot=True)
    plt.tight_layout()
    plt.title('Correlation Matrix of Various Features and Book Rating')
    plt.savefig('correlation_matrix.png', dpi=300)
    plt.show()

#books = pd.read_csv('book_data.csv',error_bad_lines = False)
#get_correlation_matrix(books)