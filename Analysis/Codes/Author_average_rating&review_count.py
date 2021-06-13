import numpy as np # linear algebra
import pandas as pd # data processing
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
import seaborn as sns

'''
Plot Authors' average rating
Plot Authors' rate count and review count
read from good_reads_final
'''

df = pd.read_csv('good_reads_final.csv')

assert isinstance(df,pd.DataFrame)

df.info()

df_count_author = df.groupby(df['author_id']).agg({'author_id':'count'})
df_unique_autor = df['author_id'].unique()
new_df = pd.DataFrame(df_unique_autor)
len_group_author = len(new_df.index)
len_non_group_author = len(df.index)

df_top_ratings =   df[(df['score']>df['score'].quantile(0.9))
                    & (df['author_average_rating']>df['author_average_rating'].quantile(0.9)) 
                    & (df['author_rating_count']>df['author_rating_count'].quantile(0.9))
                    & (df['author_review_count']>df['author_review_count'].quantile(0.9))
                    & (df['book_average_rating']>df['book_average_rating'].quantile(0.9))
                    & (df['num_ratings']>df['num_ratings'].quantile(0.8))]

df_top_ratings = df_top_ratings.sort_values(by=['author_average_rating'])

fig_dims = (14, 7)
fig, ax = plt.subplots(figsize=fig_dims,frameon=False)
ax = sns.barplot(x="author_average_rating", y="author_name", data=df_top_ratings, palette="Blues_d")

ax.set_xlim(4.1,4.6)
for p in ax.patches:
    ax.annotate(format(p.get_width(), '.2f'), 
                   ( p.get_width()*1.003 , p.get_y() + p.get_height() + 0.1), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')
plt.savefig('author_ratings.png',dpi = 200)

df_counts =   df[((df['author_rating_count']+df['author_review_count']) > 3e+6)]
df_counts["counts"] = df_counts['author_rating_count']+df_counts['author_review_count']
df_counts = df_counts.sort_values(by=['counts'])

f, ax = plt.subplots(figsize = (20,10))
sns.set_color_codes('pastel')
sns.barplot(x = 'counts', y = 'author_name', data = df_counts,
            label = 'Rate Count', palette = 'Blues_d', edgecolor = 'w')
sns.set_color_codes('muted')
sns.barplot(x = 'author_review_count', y = 'author_name', data = df_counts,
            label = 'Review Count', palette = 'YlOrBr', edgecolor = 'w')
ax.legend(ncol = 2, loc = 'upper right')
sns.despine(left = True, bottom = True)
plt.show()
