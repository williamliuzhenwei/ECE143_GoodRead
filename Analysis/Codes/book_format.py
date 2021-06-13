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

def get_top_5_book_formats(df):
    '''
    desc: plots top 5 book formats, as well as 
    a plot overlaying the rating groups over the top 5 book formats
    
    :param df: books dataframe, made from reading .csv file of data
    :type df: dataframe
    '''
    assert isinstance(df, pd.DataFrame)
    books = df
    # QUERY: BOOK FORMAT VS RATINGS
    book_form = np.array(books['book_format'])
    book_form_dict = {}
    for x in book_form:
        if x not in book_form_dict:
            book_form_dict[x] = 1
        elif x in book_form_dict:
            book_form_dict[x] += 1
    #print(book_form_dict)
    # get top 10 book formats
    sorted_form_dict = {}
    sorted_keys2 = sorted(book_form_dict, key=book_form_dict.get)
    for k in sorted_keys2:
        sorted_form_dict[k] = book_form_dict[k]
    #print(sorted_form_dict)
    top_ten_formats = list(sorted_form_dict)[-1]
    final_form_dict = {}

    final_form_dict = {'ebook': 2534, 'Mass Market\nPaperback': 2668, 'Kindle Edition': 5436, 'Hardcover': 12163, 'Paperback': 28725}
    keys2 = final_form_dict.keys()
    values2 = final_form_dict.values()

    x = list(keys2)
    y = list(values2)
    barlist2= plt.barh(x, y,color='#f4811d')
    color_arr = ['#fff4b6', '#feda7e', '#feb23f', '#f4811d', '#d55607', '#a03704']
    barlist2[0].set_color(color_arr[1])
    barlist2[1].set_color(color_arr[2])
    barlist2[2].set_color(color_arr[3])
    barlist2[3].set_color(color_arr[4])
    barlist2[4].set_color(color_arr[5])

    plt.title('Top 5 Book Formats')
    plt.xlabel('Number of Books')
    for i in range(my_cmap.N):
        rgba = my_cmap(i)
    plt.tight_layout()
    plt.savefig('top_5_book_formats.png', dpi=300)

    # BOOK RATINGS VS BOOK FORMAT
    book_format_list = np.zeros(len(books['book_format'])) # keys are 
    paperback_count = 0
    hardcover_count = 0
    kindle_count = 0
    mmp_count = 0
    ebook_count = 0
    other_count = 0
    book_form_list = []

    #books = books.sort_index(axis=0,ascending=True)
    #books['genres_spanned'] = genre_span_arr
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
    #books.head()
    books['rate_group'] = pd.cut(books['book_rating'],bins=[0,3,3.5,4,4.5,5], labels=['Poor (0-3)','Bad (3-3.5)','Decent (3.5-4)', 'Good (4-4.5)','Extremely Good (4.5-5)'])
    sss = books.groupby(['books_format', 'rate_group'])['genres'].size().unstack()
    ax = sss.plot(kind='bar', stacked=True, title = 'Ratings of Books vs Top 5 Book Formats',colormap=my_cmap)
    plt.legend(loc="upper right")
    plt.tight_layout()
    plt.xlim(0.5, 5.5)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(['Paperback', 'Hardcover', 'Kindle Edition', 'Mass Market\n Paperback', 'ebook'], rotation=0)
    ax.set_xlabel('Book Formats\n')
    plt.savefig('book_format_vs_rating_final.png', dpi=300)
    plt.show()

#books = pd.read_csv('book_data.csv',error_bad_lines = False)
#get_top_5_book_formats(books)