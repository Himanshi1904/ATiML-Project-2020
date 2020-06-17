import re
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import tokenize
import numpy as np
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from lexical_diversity import lex_div as ld
from nltk.util import ngrams
import gensim
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import os
import codecs
import re
import string
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from collections import Counter
from collections import OrderedDict
# import nlp
import spacy
from textstat.textstat import textstatistics, legacy_round
import en_core_web_sm
nlp = en_core_web_sm.load()


data = pd.read_csv(
    "/Users/nandish21/Downloads/1-Masters/2nd-Sem/ATML/Project/git/git_version_1/ATiML-Project-2020/ProjectCode/export_dataframe2.csv",
    encoding="ISO-8859-1")

# Split Train and Test Data
y_true = data['class'].values
x_train, test_df, y_train, y_test = train_test_split(data, y_true, stratify = y_true, test_size = 0.2)
train_df, cv_df, y_train, y_cv = train_test_split(x_train, y_train, stratify = y_train, test_size = 0.2)

print("Number of samples in training data :", train_df.shape[0])
print("Number of samples in validation data :", cv_df.shape[0])
print("Number of samples in test data :", test_df.shape[0])

train_class_distribution = train_df['class'].value_counts().sort_index()
cv_class_distribution = cv_df['class'].value_counts().sort_index()
test_class_distribution = test_df['class'].value_counts().sort_index()

print("\ntraining distribution:\n\n", train_class_distribution)
print("\ncv distribution: \n\n", cv_class_distribution)
print("\ntest distribution: \n\n", test_class_distribution)

# X_train, X_test, y_train, y_test = train_test_split(dfFeature, data['guten_genre'], test_size=0.3)

clf = MultinomialNB(alpha=.45)
clf.fit(train_df, y_train)
pred = clf.predict(test_df)
#
print('*******************F1 Score and Accuracy*****************************')
print('F1 Score: ', metrics.f1_score(y_test, pred, average='macro'))
print('Accuracy: ', metrics.accuracy_score(y_test, pred))