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

def get_title_len(df):
    '''
    desc: plots title word length distribution
    with overlaid rating groups
    
    :param df: books dataframe, made from reading .csv file of data
    :type df: dataframe
    '''
    assert isinstance(df, pd.DataFrame)
    books = df
    # BOOK RATINGS VS NUMBER OF LETTERS IN TITLE
    title_len_list = np.zeros(len(books['book_title']))
    for x in books['book_title'].index:
        num_title_words = int(len(str(books['book_title'][x]).split()))
        title_len_list[x] = num_title_words
    #print(title_len_list)
    title_len_arr = np.array(title_len_list)
    books['title_word_len'] = title_len_arr
    books['rate_group'] = pd.cut(books['book_rating'],bins=[0,3,3.5,4,4.5,5], labels=['Poor (0-3)','Bad (3-3.5)','Decent (3.5-4)', 'Good (4-4.5)','Extremely Good (4.5-5)'])
    ss = books.groupby(['title_word_len', 'rate_group'])['genres'].size().unstack()
    ss.plot(kind='bar', stacked=True, title = 'Ratings of Books vs Number of Words in Title',colormap=my_cmap)
    plt.axvline(x= np.mean(books['title_word_len']), color="navy", label="mean")
    plt.legend(loc="upper right")
    plt.xlim(-0.5, 14.5)
    plt.xlabel('Number of Words in Book Title')
    plt.tight_layout()
    plt.savefig('book_word_len_vs_rating.png', dpi=300)
    plt.show()

#books = pd.read_csv('book_data.csv',error_bad_lines = False)
#get_title_len(books)