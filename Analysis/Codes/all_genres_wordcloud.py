from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

books = pd.read_csv('book_data.csv',error_bad_lines = False)
g= []
for i in range(books.shape[0]):
    if isinstance(books['genres'].iloc[i], str) and len(books['genres'].iloc[i])>0:
        g.append(books['genres'].iloc[i])
#figuring out all the existing genres and saving the genres in Genres_list list
Genres_dict = {}
for i in range(len(books)):
    row = books.iloc[i]
    Gen = str(row.genres)
    genres = Gen.split('|')
    for genre in genres:
        if genre not in Genres_dict:
            Genres_dict[str(genre)] = 1
        else:
            Genres_dict[str(genre)] +=1
#len(Genres_list)

#word_could_dict=Counter(g)
custom_mask = np.array(Image.open("book.png"))
wordcloud = WordCloud(background_color="white", collocations=False, mask=custom_mask, contour_width=1, contour_color='gray').generate_from_frequencies(Genres_dict)
#wc = WordCloud(background_color="white", mask=custom_mask)
#wc = WordCloud(background_color="white", collocations=False, mask=custom_mask, contour_width=1, contour_color='gray')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.savefig("wc143.png")
plt.show()
