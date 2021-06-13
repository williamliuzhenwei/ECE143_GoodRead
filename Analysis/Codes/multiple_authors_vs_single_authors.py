import pandas as pd
import numpy as np
books = pd.read_csv('book_data.csv',error_bad_lines = False)

authors = np.unique(books["book_authors"])
more_than_one_author_indices = []
for i in range(len(books)):
    if "|" in books["book_authors"].iloc[i]:
        more_than_one_author_indices.append(i)
mtoai_rating = 0
for i in more_than_one_author_indices:
    mtoai_rating+= books['book_rating'].iloc[i]
print(mtoai_rating/len(more_than_one_author_indices))
#4.051466890192806
print(np.mean(books['book_rating']))
#4.020027255483324

#future: each individual authors work compared to collaborated ones
