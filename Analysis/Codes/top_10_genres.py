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
my_cmap2 = ListedColormap(sns.color_palette('Blues_d'))
from matplotlib.colors import Normalize

def get_top_10_genres(df):
    '''
    desc: takes dataframe genres column, identifies unique genres and number of books
    that fall within them, and plots a bargraph with the top 10 genres

    :param df: books dataframe, made from reading .csv file of data
    :type df: dataframe
    '''

    # parse through genres to idenify unique categories
    genre_arr = np.array(books['genres'])
    #print(genre_arr)
    unique_genres = []
    ave_genres_per_book = 0
    total_num_books = 0

    for indx in genre_arr:
        string = str(indx)
        temp = string.split("|")
        ave_genres_per_book += len(temp)
        total_num_books += 1
        for i in temp:
            if i not in unique_genres:
                unique_genres.append(i)
    
    # make dictionary where the keys are the unique genres and the values are the count of books that satisfy that genre
    genres_dict = dict.fromkeys(unique_genres, 0)
    # find book count that falls under every unique genres
    for indx in genre_arr:
        string = str(indx)
        temp = tuple(string.split("|"))
        for gen in temp:
            genres_dict[gen] += 1
    # sort genres dict
    sorted_dict = {}
    sorted_keys = sorted(genres_dict, key=genres_dict.get)
    for k in sorted_keys:
        sorted_dict[k] = genres_dict[k]

    # get top 10 genres only for plotting bar graph
    top_ten_genres = list(sorted_dict)[-11:-1]
    final_genres_dict = {}
    for i in top_ten_genres:
        final_genres_dict[i] =(sorted_dict[i])
    keys = final_genres_dict.keys()
    values = final_genres_dict.values()
    values_list = list(values)

    x1 = list(keys)
    y1 = list(values)
    # make horizontal bar plot to be more consistent style with other bar plots
    barlist = plt.barh(x1, y1)
    # use custom color palette to match with genres vs ratings vs frequency bubble plot
    colors = ["Crimson", "LightSalmon", "#FFFF00", "#663399", "Orange", "#90EE90", "#808000", "#1E90FF", "#0000FF", "#DAA520", "#228B22", "red", "#3CB371"]
    barlist[0].set_color(colors[1])
    barlist[1].set_color(colors[2])
    barlist[2].set_color(colors[3])
    barlist[3].set_color(colors[4])
    barlist[4].set_color(colors[5])
    barlist[5].set_color(colors[6])
    barlist[6].set_color(colors[7])
    barlist[7].set_color(colors[8])
    barlist[8].set_color(colors[9])
    barlist[9].set_color(colors[10])
    plt.title('Top 10 Book Genres')
    plt.xlabel('Number of Books')
    plt.savefig('top_10_genres.png', dpi=300)
    plt.show()

