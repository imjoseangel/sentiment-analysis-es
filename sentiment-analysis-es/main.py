#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from numpy import negative

import pandas as pd
from sklearn.naive_bayes import MultinomialNB


def main():
    # Read the data from CSV file
    sentiments = pd.read_csv('data/sentiments.csv', sep=',')
    emotions = pd.read_csv('data/emotions.csv', sep=',')

    positive = sentiments[sentiments['polarity'] == 'positive']
    negative = sentiments[sentiments['polarity'] == 'negative']

    print(positive)
    print(negative)


if __name__ == '__main__':
    main()
