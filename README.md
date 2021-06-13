# ECE143_project (Group 2): Goodreads Authors and Books Analysis
*Team Members: Anirudh, Fatemeh, Samantha, Zhenwei*

**Background**
Since the COVID-19 pandemic has caused us to isolate and quarantine to promote 
overall wellbeing and safety, books have become an extremely important and 
meaningful pastime for many. We wanted to analyze trends about different
authors and books in the hopes of creating tools that may help all book-lovers
identify their next favorite read.

We analyzed multiple datasets from Kaggle and other sources to learn more about
Authors (where they are mostly located, who in particular are the most popular/influential,
etc.) as well as books (if any specific features - genre diversity, book format,
etc. - correlated with book rating. We also looked into how the most frequent
words in a books' title can help predict its' genre.

In this repository we have included all the relevant parts of our project: 
the datasets, a Jupyter notebook that can be run to obtain our plots, `.py` files,
our final powerpoint that provides a nice visual overview of our findings, etc.
Please see below for more information about this repository organization and
how to properly run our Notebook.


**Structure of files**


- **Analysis**
    - **Codes** `.py` files
        - **Authors** | **Genres** | **Books Features**
    - **Datasets**
    - **images**
         - plots we have generated from our data analysis
    
- **PDF of Slides**
    -  titled Group2_ppt_final.pdf
- **Jupyter Notebook** (Code.ipynb)
- **Website**
    - **Website**
    - **Images**
- **Timeline**
- **Method Test Cases Assignment**
    -  the file is named "Group-2_Assignment-1.ipynb"


**Running our code**

We have uploaded the Jupyter notebook containing all genres in the main page and also the `.py` files for each plot/querry in the Analysis folder 

STEPS TO RUN OUR NOTEBOOK:
- (1) Clone/Download our repository 
```
git clone https://github.com/Fasgarinejad/ECE143_project
```
- (2) After the download has finished, unzip the file 'ECE143_project-main' and expand it to follow filepath: Analysis > Datasets
- (3) Download all the files in the Dataset folder ('good_reads_final.csv' and 'books.csv' are already downloaded, but you need to unzip 'book_data.csv.zip' and click the README.md to get a link to download 'final_dataset.csv')
- (4) create a new folder and move all four .csv files into it.
- (5) drag the 'Code.ipynb' Jupyter notebook (found in main file directory) into the same new folder you have created in the last step
- (6) open Terminal, and type in the command 'jupyter notebook'. a window should pop up and follow the file path to get to where your 'Code.ipynb' and click to open it
- (7) make sure to pip or conda install the 3rd party modules we have listed below 
- (8) Run our Jupyter Notebook

Note: We are using this version of Python:
```
Python 3.8 
```

**All Third-party modules we have used**

Main ones:

- matplotlib
- pandas
- sklearn
- numpy
- nltk
- wordcloud #!conda install -c conda-forge wordcloud=1.6.0 

Dataframe import, filtering and analysis, math, etc.
1. Pandas #for importing csv file and working with dataframes
2. Numpy #for sum mathematical stuff in the dataframes
3. csv #for opening datafiles and reading them into dataframes
4. collections #for OrderedDict, sort dict
5. random #for generating random numbers for random colors 
6. time #For calculating time spent for prediction
7. import re
8. import collections
9. from collections import Counter

Plotting 

10. matplotlib #for plotting
11. from PIL import Image
12. import seaborn as sns 
13. seaborn #to add more plot features and layout
14. basemap

Wordcloud

15. from wordcloud import WordCloud
16. from wordcloud import WordCloud, ImageColorGenerator


Genre Classification and language processing

17. nltk  #for string analysis (stopwords, punctuations, etc.)
18. string #for working with string data
19 . import sklearn
20. from sklearn.preprocessing import StandardScaler
21. from sklearn.ensemble import RandomForestClassifier #Random Forest
22. from sklearn.pipeline import make_pipeline
23. from sklearn.svm import SVC
24. from sklearn.model_selection import train_test_split
25. from sklearn.metrics import accuracy_score
26. from sklearn.model_selection import ShuffleSplit
27. from sklearn.ensemble import RandomForestClassifier
28. from sklearn.datasets import make_classification
29. from sklearn.ensemble import RandomForestClassifier #Random Forest

**Some of our plots**

Title Classification accurracy using RF, SVM and KNN<br><img src="https://github.com/Fasgarinejad/ECE143_project/blob/main/Analysis/images/prediction.png" width="500">

Methodology:

1) Stored titles of books in `Sports`, `Classics` and `Romance` genres
1) Picked 150 most frequent words in the titles of each genre
2) Aggregated all the 150*3 most frequent words, some were redundant
3) Omitted non-English, Punctuations and stopwords
4) Created word frequency vectors for each title

Model creation

5) input of the model: independent variables: word vectors | dependent variable: genre (`Sports` | `Classics` | `Romance`) one hot encoded, So (0 | 1 | 2)
6) Splitted the data to training and test set with a ratio of 30 percent test 
7) Trained SVM, RF and KNN on the training set 10 times (iteration on train-test split) and used the predicted model on the test set

Result: SVM classifies the titles with an average accuracy of 70.4 percent.


Authors' birthplace from 16th to 21th <br><img src="https://github.com/Fasgarinejad/ECE143_project/blob/main/Analysis/images/authors_nationality_over_years.gif" width="500">


Count of Authors for different countries 1800-1980<br><br><img src="https://github.com/Fasgarinejad/ECE143_project/blob/main/Analysis/images/countries_gif.gif" width="500">
