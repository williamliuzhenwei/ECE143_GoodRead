import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
import csv
from pandas import DataFrame
import seaborn as sns
from IPython.display import HTML
import collections

'''
Plot each countries' unique genres
Read from final_dataset.csv
'''

df = pd.read_csv('final_dataset.csv',error_bad_lines = False) 

assert isinstance(df,pd.DataFrame)

df_map = df.drop(columns=['authorid','about','website','twitter','original_hometown'])
#Drop the unwanted columns in the dataset
df = df.drop(columns=['authorid','about','website','twitter','original_hometown','latitude','longitude'])
df = df[df['born'].notna()]
df = df[df['country'].notna()]
df = df[df['genre'].notna()]
df = df.reset_index(drop=True)
df = df.sort_values(by=['country'])
df = df.reset_index(drop=True)
df_country_genre = df[['country','genre']]
df_country_genre.head()
from collections import Counter
def split_genre(df_c):
    b = DataFrame(df_c.genre.str.split(',').tolist(), index=df_c.country).stack()
    b = b.reset_index()[[0, 'country']] # var1 variable is currently labeled 0
    b.columns = ['genre', 'country'] # renaming var
    
    b = collections.Counter(b.genre).most_common(8)
    # df_counts_top
    b = pd.DataFrame(b, columns = ['genre','count'])
#     b = b.sort_values(by = ['count'])
    b['count'] = b['count']/max(b['count'])
    b['genre'] = b.genre.str.title()
    
    # Initialing the spiderplot by  
    # setting figure size and polar 
    # projection 
    df_counts_top = b#.sample(frac=1).reset_index(drop=True)
    plt.figure(figsize =(15, 10)) 
    plt.subplot(polar = True) 

    theta = np.linspace(0, 2 * np.pi, len(df_counts_top)+1) 

    # Arranging the grid into number  
    # of sales into equal parts in 
    # degrees 
    lines, labels = plt.thetagrids(range(0, 360, int(360/len(df_counts_top['genre']))), 
                                                             list(df_counts_top['genre'])) 

    # Plot actual sales graph 
    plt.plot(theta, list(df_counts_top['count'])+[df_counts_top['count'][0]], color='#1aaf6c') 
    plt.fill(theta, list(df_counts_top['count'])+[df_counts_top['count'][0]], color='#1aaf6c', alpha=0.25) 
    plt.yticks(color='grey', size=25)
    plt.xticks(color='black', size=30)

    # # Add legend and title for the plot 
#     plt.title(country, size = 30) 
    plt.text(4.73,0.45,country,color = 'grey',  weight='medium', size=50, horizontalalignment='center', verticalalignment='top')
    plt.savefig(country + '.png')

    # # Dsiplay the plot on the screen 
#     plt.show() 
    
    return plt.show()

country = 'United States'
df_country = df_country_genre[df_country_genre['country']==country]
df_counts_top = split_genre(df_country)


country = 'France'
df_country = df_country_genre[df_country_genre['country']==country]
df_counts_top = split_genre(df_country)

country = 'India'
df_country = df_country_genre[df_country_genre['country']==country]
df_counts_top = split_genre(df_country)

country = 'China'
df_country = df_country_genre[df_country_genre['country']==country]
df_counts_top = split_genre(df_country)

country = 'Saudi Arabia'
df_country = df_country_genre[df_country_genre['country']==country]
df_counts_top = split_genre(df_country)

country = 'Japan'
df_country = df_country_genre[df_country_genre['country']==country]
df_counts_top = split_genre(df_country)
