import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import csv
import seaborn as sns
import statistics as stat
import collections
from numpy.random import rand

def get_book_rating_distribution(df):
    '''
    desc: plots the distrbution of all book ratings from 'book_rating' column of dataframe

    :param df: books dataframe, made from reading .csv file of data
    :type df: dataframe
    '''
    assert isinstance(df, pd.DataFrame)
    # book ratings distribution
    sns.displot(books, x='book_rating',binwidth = 0.05, color = 'salmon')
    plt.axvline(x= np.mean(books['book_rating']), color="blue", label="mean")
    plt.title('Distribution of All Books\' Ratings' )
    plt.legend(loc="upper left")
    plt.xlim(3,5)
    plt.tight_layout()
    plt.savefig('ratings_distrbution.png', dpi=300)
    plt.show()

#books = pd.read_csv('book_data.csv',error_bad_lines = False)
#get_book_rating_distribution(books)