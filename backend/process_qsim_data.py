# encoding=utf8
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"

sys.path.append('..')

import time
import pandas as pd
import tensorflow as tf
from collections import defaultdict
import random
import numpy as np
import collections
import math
import utils
import re
from tempfile import gettempdir
import nltk

vocabulary_size = 50000
max_num_articles = 700
w2v_dim = 50
data_folder = "data/financial-news-dataset/bloomberg/"

dataset_articles = []  # list of strings where each string is article
dataset_sents = []  # list of sentences where each sentence is a list of strings
dataset_words = []  # list of strings where each string is a word

# count = defaultdict(int)

# def get_corpus():
#     dataset_articles = []  # list of strings where each string is article
#     dataset_sents = []  # list of sentences where each sentence is a list of strings
#     dataset_words = []  # list of strings where each string is a word

#     files_read = 0
#     for subdir, dirs, _ in os.walk(data_folder):
#         for dir in dirs:
#             for file_folder, _, files in os.walk(os.path.join(subdir, dir)):
#                 for file in files:
#                     if files_read >= max_num_articles:
#                         return dataset_articles, dataset_sents, dataset_words
#                     filename = os.path.join(file_folder, file)
#                     with open(filename, "r") as f_in:
#                         print files_read
#                         files_read += 1
#                         file_str = "\n".join(
#                             f.strip() for f in f_in if not (f.startswith("--") or not f or f.isspace())).decode("utf-8")
#                         sent_list = nltk.sent_tokenize(file_str)
#                         dataset_sents.append(sent_list)
#                         word_list = nltk.word_tokenize(file_str)
#                         dataset_words.extend(word_list)
#                         for w in word_list:
#                             count[w] += 1
#                         dataset_articles.append(file_str)

# dataset_articles, dataset_sents, dataset_words = get_corpus()

# print dataset_sents
# with open("bloombergconcat.txt", "w") as f:
#     a = "\n".join(k[0] for k in dataset_sents)
#     f.write(a)

# dataset_articles, dataset_sents, dataset_words = get_corpus()
# vocabulary_size = min(len(count), vocabulary_size)
# print "Finished dataset processing ", len(dataset_articles), len(dataset_words)

from gensim.models import Word2Vec, word2vec

vocab = word2vec.LineSentence("bloombergconcat.txt")
w2v = Word2Vec(vocab)

data_loc = "data/quora.tsv"
import pandas as pd

data_pd = pd.read_csv(data_loc, sep="\t")
print data_pd

labels = data_pd["is_duplicate"].tolist()
q1 = data_pd["question1"].tolist()
q2 = data_pd["question2"].tolist()

data_1 = []
data_2 = []

def process_sent(sent):
    if not isinstance(sent, str) or not sent:
        return np.array([0.0] * 100)
    mat = []
    for w in nltk.word_tokenize(sent.decode("utf-8")):
        if w in w2v:
            mat.append(w2v[w])
    mat = np.array(mat)
    if len(mat) == 0:
        return np.array([0.0] * 100)
    return mat.mean(axis=1, keepdims=True)

# data_1 = [process_sent(s) for s in q1]
# data_2 = [process_sent(s) for s in q2]

# data_1

# train_set_1 = data_1[0:int(len(data_1) * 2/3)]
# train_set_2 = data_2[0:int(len(data_2) * 2/3)]
# train_labels = labels[0:int(len(labels) * 2/3)]

# test_set_1 = data_1[int(len(data_1) * 2/3):len(data_1) - 1]
# test_set_2 = data_2[int(len(data_2) * 2/3):len(data_2) - 1]
# test_labels = labels[int(len(labels) * 2/3):len(labels) - 1]

# train_set = np.hstack([train_set_1, train_set_2])
# test_set = np.hstack([test_set_1, test_set_2])

# from keras.preprocessing import sequence
# from keras.models import Sequential
# from keras.layers import Dense, Embedding, Flatten, Merge, Dropout
# from keras.layers import LSTM
# from keras.datasets import imdb

# max_features = 20000
# maxlen = 80  # cut texts after this number of words (among top max_features most common words)
# batch_size = 32

# model2 = Sequential()
# model2.add(Dense(200, input_shape=(200, 1)))
# model2.add(Dropout(0.1))
# model2.add(Dense(64))
# model2.add(Dropout(0.1))
# model2.add(Dense(32))
# model2.add(Dropout(0.1))
# model2.add(Dense(1, activation='sigmoid'))

# model2.compile(loss='binary_crossentropy',
#               optimizer='adam',
#               metrics=['accuracy'])

# print('Train...')
# model2.fit(train_set, train_labels,
#           batch_size=batch_size,
#           epochs=15,
#           validation_data=(test_set, test_labels))
# score, acc = model2.evaluate(test_set, test_labels,
#                             batch_size=batch_size)
# print('Test score:', score)
# print('Test accuracy:', acc)


def sim(s1, s2):
    from sklearn.metrics.pairwise import cosine_similarity
    s1_mat = process_sent(s1)
    s2_mat = process_sent(s2)
    return cosine_similarity(s1_mat, s2_mat)



