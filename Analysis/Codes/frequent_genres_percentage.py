from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

books = pd.read_csv('book_data.csv',error_bad_lines = False)

colors = ["Crimson", "LightSalmon", "#FFFF00", "#663399","Orange", "#90EE90", "#808000",
                "#1E90FF", "#0000FF", "#DAA520", "#228B22", "red", "#3CB371"]

# create dataset
#also can be derived from our function in part 1
most_frequent_gens ={'Contemporary': 6039,
 'Classics': 6272,
 'Historical Fiction': 6399,
 'Science Fiction': 6780,
 'Nonfiction': 7598,
 'Mystery': 7902,
 'Paranormal': 7994,
 'Historical': 10789,
 'Young Adult': 11251,
 'Romance': 18636,
 'Fantasy': 23583,
 'Fiction': 25736}
height = [i/len(books)*100 for i in list(most_frequent_gens.values())]
bars = list(most_frequent_gens.keys())
y_pos = np.arange(len(bars))

# Create horizontal bars
plt.barh(y_pos, height,color=colors)
plt.xlabel("Percentage")
plt.ylabel("Genre")
plt.title("Percentage of Each Genre in the Total dataset")

# Create names on the x-axis
plt.yticks(y_pos, bars)

# Show graphic
#plt.show()
plt.savefig("percentage_genre.png")
