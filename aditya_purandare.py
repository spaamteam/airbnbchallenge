#!/usr/bin/env python

import numpy as np
import pandas as pd

print("Howdy, Aggies!")

# files = ['countries.csv', 'sessions.csv', 'age_gender_bkts.csv', 'train_users.csv', 'test_users.csv']

# Lighter version of file import
files = ['countries.csv', 'age_gender_bkts.csv', 'train_users.csv', 'test_users.csv']
data_frame = {}

for file in files:
    # Data scientists use the convention to put data files into "fixtures" folder
    data_frame[file.replace('.csv', '')] = pd.read_csv('fixtures/' + file)

train = data_frame['train_users']
test = data_frame['test_users']
train = train.fillna(-1)
test = test.fillna(-1)

if __name__ == '__main__':
    labels = train['country_destination'].values
    print(labels)

    print("Program finished")

    #Added a comment to indicate program ended
