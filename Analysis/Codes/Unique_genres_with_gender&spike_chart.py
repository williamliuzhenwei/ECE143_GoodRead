import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import seaborn as sns

'''
Plot Male and Female authors For all genres
And spike chart for 20th century genres
Read from good_reads_final.csv
'''

df = pd.read_csv('good_reads_final.csv')

assert isinstance(df,pd.DataFrame)

df.info()

unique_genres = []
genre_1 = list(df['genre_1'])
genre_2 = list(df['genre_2'])
for genre in genre_1:
    if len(genre)>0 and genre not in unique_genres:
        unique_genres.append(genre)
for genre in genre_2:
    if len(genre)>0 and genre not in unique_genres:
        unique_genres.append(genre)

temp_df_1= df[df['genre_1'] == genre] #rows with the genre_1 column=genre
temp_df_2 = df[df['genre_2'] == genre]#rows with the genre_2 columns=genre
concatinated = pd.concat([temp_df_1,temp_df_2], axis=0) #concatinate the two dataframes
len(concatinated) ==len(temp_df_1) + len(temp_df_2)
df_gif = concatinated[['genre_1','genre_2','publish_date']]
female = concatinated[concatinated['author_gender']=='female']
male = concatinated[concatinated['author_gender']=='male']
print("There are {} women and {} men in genre {}".format(len(female), len(male), genre))
genres_women_men = {}
for genre in unique_genres:
    temp_df_1= df[df['genre_1'] == genre] #rows with the genre_1 column=genre
    temp_df_2 = df[df['genre_2'] == genre]#rows with the genre_2 columns=genre
    concatinated = pd.concat([temp_df_1,temp_df_2], axis=0) #concatinate the two dataframes
    female = concatinated[concatinated['author_gender']=='female']
    male = concatinated[concatinated['author_gender']=='male']
    genres_women_men[genre] = [len(female), len(male)]

new_dict = {'Genre':[], 'Females':[], 'Males':[], 'Total':[]}
for key,value in genres_women_men.items():
    new_dict['Genre'].append(key)
    new_dict['Females'].append(value[0])
    new_dict['Males'].append(value[1])
    new_dict['Total'].append(value[1]+value[0])

df_counts = pd.DataFrame.from_dict(new_dict)
df_counts.sort_values(by=['Total'])

df_counts_top = df_counts.sort_values(by=['Total']).tail(30)
df_counts_top['unknown'] = df_counts_top['Males']/10

f, ax = plt.subplots(figsize = (15,8))
sns.set_color_codes('pastel')
sns.barplot(x = 'Total', y = 'Genre', data = df_counts_top,
            label = 'Males', palette = 'Blues_d', edgecolor = 'w')
sns.set_color_codes('muted')
sns.barplot(x = 'Females', y = 'Genre', data = df_counts_top,
            label = 'Females', palette = 'YlOrBr', edgecolor = 'w')
sns.barplot(x = 'unknown', y = 'Genre', data = df_counts_top,
            label = 'Other', color = 'grey', edgecolor = 'w')
ax.legend( loc = 'upper right')
sns.despine(left = True, bottom = True)
plt.savefig('gender.png')

plt.show()

df_counts_top = df_counts_top.sample(frac=1).reset_index(drop=True)
plt.figure(figsize =(10, 10)) 
plt.subplot(polar = True) 
    
theta = np.linspace(0, 2 * np.pi, len(df_counts_top)+1) 
    
# Arranging the grid into number  
# of sales into equal parts in 
# degrees 
lines, labels = plt.thetagrids(range(0, 360, int(360/len(df_counts_top['Genre']))), 
                                                         list(df_counts_top['Genre'])) 
    
# Plot actual sales graph 
plt.plot(theta, list(df_counts_top['Total'])+[df_counts_top['Total'][0]]) 
plt.fill(theta, list(df_counts_top['Total'])+[df_counts_top['Total'][0]], 'b', alpha = 0.1) 
    
# # Add legend and title for the plot 
plt.title("Genres for 20th Century") 
    
# # Display the plot on the screen 
plt.show() 
