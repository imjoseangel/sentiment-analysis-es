#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)

import pandas as pd
import numpy as np


def main():
    # Read the data from CSV file
    data = pd.read_csv('data/spanish_sentiment.csv', sep=',')
    print(data.head())


if __name__ == '__main__':
    main()
