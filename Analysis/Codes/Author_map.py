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
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

'''
Plot the born places of each authors on the map using longitude and latitude
Read from final_dataset.csv
'''

df = pd.read_csv('final_dataset.csv',error_bad_lines = False) 

assert isinstance(df,pd.DataFrame)

df_map = df.drop(columns=['authorid','about','website','twitter','original_hometown'])
df_map = df_map.drop(columns=['workcount','fan_count','gender','image_url','born','died',
                              'influence','average_rate','rating_count',
                              'review_count','genre','country'])
df_map = df_map[df_map['latitude'].notna()]
df_map = df_map.reset_index(drop=True)
x = df_map['latitude']
y = df_map['longitude']

from itertools import chain

def draw_map(m, scale=0.2):
    # draw a shaded-relief image
    m.shadedrelief(scale=scale)
    
    # lats and longs are returned as a dictionary
    lats = m.drawparallels(np.linspace(-90, 90, 13))
    lons = m.drawmeridians(np.linspace(-180, 180, 13))

    # keys contain the plt.Line2D instances
    lat_lines = chain(*(tup[1][0] for tup in lats.items()))
    lon_lines = chain(*(tup[1][0] for tup in lons.items()))
    all_lines = chain(lat_lines, lon_lines)
    
    # cycle through these lines and set the desired style
    for line in all_lines:
        line.set(linestyle='-', alpha=0.3, color='w')

fig = plt.figure(figsize=(18, 16), edgecolor='w')
m = Basemap(projection='cyl', resolution=None,
            llcrnrlat=-90, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, )
x, y = m(df_map['longitude'],df_map['latitude'])
plt.plot(x, y, 'ok', markersize=1)
draw_map(m)

