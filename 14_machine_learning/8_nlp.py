"""
Natural Language Processing

pip3 install nltk
"""
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

# nltk.download_shell()

messages = [line.rstrip() for line in open('SMSSpamCollection')]

print(len(messages))

for mess_no,message in enumerate(messages[:10]):
    print(mess_no,message)
    print()

messages = pd.read_csv('SMSSpamCollection',sep='\t',names=['label','message'])

print(messages)

print()
print(messages.describe())

print()
print(messages.groupby('label').describe())

messages['length'] = messages['message'].apply(len)
print(messages.head())

messages['length'].plot.hist(bins=50)
plt.show()

print(messages[messages['length'] == 910]['message'].iloc[0])

messages.hist(column='length',by='label',bins=60,figsize=(12,4))
plt.show()

print()
mess = 'Sample message! Notice: it has punctuation.'
print(string.punctuation)

nopunc = [c for c in mess if c not in string.punctuation]

print(nopunc)

print()
print(stopwords.words('english'))

nopunc = ''.join(nopunc)

clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
print(clean_mess)


def text_process(mess):
    """
    1. remove punc
    2. remove stop words
    3. return list of clean text words
    """
    nopunc = [char for char in mess if char not in string.punctuation]

    nopunc = ''.join(nopunc)

    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


messages['message'].head(5).apply(text_process)

bow_transformer = CountVectorizer(analyzer=text_process).fit(messages['message'])
print(len(bow_transformer.vocabulary_))

messages_bow = bow_transformer.transform(messages['message'])
print('Shape of the Sparse MAtrix: ',messages_bow.shape)

