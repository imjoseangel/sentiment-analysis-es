#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sklearn.naive_bayes import MultinomialNB
import re
import pandas as pd

from nltk.stem.porter import *
from numpy import negative


def stem_words(words: list) -> list:

    stemmer = PorterStemmer()
    return stemmer.stem(words)


def break_into_words(words: list) -> list:

    return re.findall("[a-zA-Z0-9]+", words)


def main():

    # Read the data from CSV file
    sentiments = pd.read_csv('data/sentiments.csv', sep=',')
    emotions = pd.read_csv('data/emotions.csv', sep=',')

    positive = sentiments[sentiments['polarity'] == 'positive']
    negative = sentiments[sentiments['polarity'] == 'negative']
    neutral = sentiments[sentiments['polarity'] == 'neutral']

    positivelst = (positive['word'].tolist())
    negativelst = (negative['word'].tolist())
    neutrallst = (neutral['word'].tolist())


if __name__ == '__main__':
    main()
