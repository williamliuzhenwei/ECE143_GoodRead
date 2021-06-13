from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image

books = pd.read_csv('book_data.csv',error_bad_lines = False)

authors_freq = {}
all_authors = []
auth_ratings ={}
for i in range(len(books)):
    authors = books['book_authors'].iloc[i].split("|")
    for auth in authors:
        all_authors.append(auth)
        if auth not in authors_freq:
            authors_freq[auth] = 1
        else:
            authors_freq[auth] +=1
for i in range(len(books)):
    authors = books['book_authors'].iloc[i].split("|")
    rating = books.iloc[i]['book_rating']
    for auth in authors:
        auth_ratings[auth]= []

for i in range(len(books)):
    authors = books['book_authors'].iloc[i].split("|")
    rating = books.iloc[i]['book_rating']
    for auth in authors:
        auth_ratings[auth].append(rating)

auth_ratings_av = {}
for k,v in auth_ratings.items():
    auth_ratings_av[k] = np.mean(v)

freqs = list(authors_freq.values())

def find_author_with_number_of_works(i, d):
    """
    i is the number of works
    """
    #assert isinstance(i, int)
    assert isinstance(d, dict)
    filtered_dict = {k:v for k,v in d.items() if v==i} #future asserrtion, comments, etc.
    return filtered_dict

i = 1
res = find_author_with_number_of_works(i, authors_freq)
max_rate = 0
chosen_author = ""
for k,v in res.items():
    if auth_ratings_av[k] >max_rate:
        max_rate = auth_ratings_av[k]
        chosen_author = k
print(chosen_author, max_rate, i)

result = [] #authors chosen
for i in sorted(np.unique(freqs)):
    res = find_author_with_number_of_works(i, authors_freq)
    max_rate = 0
    chosen_author = ""
    for k,v in res.items():
        if auth_ratings_av[k] >max_rate:
            max_rate = auth_ratings_av[k]
            chosen_author = k
    result.append((chosen_author, np.round(max_rate,2), i))


labels =  ["One", "Two", "Three", "Four", "5-20", ">20"]
sizes = [float(freqs.count(1)), freqs.count(2), freqs.count(3), freqs.count(4), 3539-freqs.count(4), 274+43]
#colors
colors = ['#593483','#E7DA57', '#5A3614', '#6CE2AC','salmon','#0015BC']

fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=45)
#draw circle
centre_circle = plt.Circle((0,0),0.75,fc='white')
#fig = plt.figure(figsize=(10, 10))
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')
plt.title("Frequency of Authors' number of books")
plt.tight_layout()
#plt.show()
plt.savefig("circle.png")
