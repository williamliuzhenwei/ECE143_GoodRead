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

df = pd.read_csv('final_dataset.csv',error_bad_lines = False) 
df_map = df.drop(columns=['authorid','about','website','twitter','original_hometown'])
#Drop the unwanted columns in the dataset
df = df.drop(columns=['authorid','about','website','twitter','original_hometown','latitude','longitude'])
df = df[df['born'].notna()]
df = df[df['country'].notna()]
df = df[df['genre'].notna()]
df = df.reset_index(drop=True)
for i in range(len(df)):
    df.loc[i,'born'] = df.loc[i,'born'][0:4]
df = df.sort_values(by=['born'])
df = df.reset_index(drop=True)
df_born = df[['born','genre']]
df_born['born'] = df_born.born.astype(int)
year_0 = 1680
i = 0
for i in range(len(list(df_born['born']))):
    if ((int(df_born['born'][i]) >= year_0) and (int(df_born['born'][i]) < year_0 + 20)):
        df_born['born'][i] = year_0
    if int(df_born['born'][i]) >= (year_0 + 20):
        year_0 = year_0 + 20
        df_born['born'][i] = year_0
b = DataFrame(df_born.genre.str.split(',').tolist(), index=df_born.born).stack()
b = b.reset_index()[[0, 'born']] # var1 variable is currently labeled 0
b.columns = ['genre', 'born'] # renaming var
df_list = b.groupby('born')['genre'].apply(list).to_dict()

list_co = df_born.genre.unique()
list_colors = []
for i in range(len(list_co)):
    

    color = 'grey'
    if list_co[i] == 'poetry':
#         color = (0.9,0.9,0.9)
        list_colors.append('r')  
    else:
        list_colors.append(color)    
    

colors = dict(zip(list_co,list_colors))

df_list_year = collections.Counter(df_list.get(1800))
dff_test = pd.DataFrame.from_dict(df_list_year.items())
dff_test[0].unique()
fig, ax = plt.subplots(figsize=(15, 8))
def draw_barchart(year):
    df_list_year = collections.Counter(df_list.get(year))
    dff = pd.DataFrame.from_dict(df_list_year.items())
    dff = dff.sort_values(by=[1]).tail(10)
#     dff = dff[['romance','history','poetry','political','religion and spirituality','crime','mystery and thrillers','biographies and memoirs','fantasy','philosophy']]
    
    # pass colors values to `color=`
    ax.clear()
    ax.barh(dff[0], dff[1], color=[colors[str(x)] for x in dff[0]])
    
    dx = dff[1].max() / 200
    for i, (value, name) in enumerate(zip(dff[1], dff[0])):
        ax.text(value+dx, i,     name.title() ,           size=14, weight=600, ha='left', va='center')
        ax.text(value-dx, i,     f'{value:,.0f}K',  size=14, weight = 600, color = 'w', ha='right',  va='center')
    # ... polished styles
    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    #ax.text(0, 1.06, 'Population (thousands)', transform=ax.transAxes, size=12, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, 'Popular Genres from 1800 to 1990',
            transform=ax.transAxes, size=24, weight=600, ha='left')
    ax.text(0, 1.06, 'Published Records (in Thousands)', transform=ax.transAxes, size=12, color='#777777')
    plt.box(False)
    
draw_barchart(1980)
import matplotlib.animation as animation
from IPython.display import HTML
fig, ax = plt.subplots(figsize=(15, 8))
animator = animation.FuncAnimation(fig, draw_barchart, frames=range(1800, 2000, 20))
HTML(animator.to_jshtml()) 
