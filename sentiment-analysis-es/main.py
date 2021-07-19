#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import pandas as pd
import numpy as np
from pandas.core.indexes import category


def main():
    # Read the data from CSV file
    sentiments = pd.read_csv('data/sentiments.csv', sep=',')
    emotions = pd.read_csv('data/emotions.csv', sep=',')
    print(sentiments.head())
    print(emotions.head())


if __name__ == '__main__':
    main()
