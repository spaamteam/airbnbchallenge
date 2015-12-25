import numpy as np
import pandas as pd

print("Howdy, Aggies!")

# files = ['countries.csv', 'sessions.csv', 'age_gender_bkts.csv', 'train_users.csv', 'test_users.csv']
# Lighter version of file import
files = ['countries.csv', 'age_gender_bkts.csv', 'train_users.csv', 'test_users.csv']
data_frame = {}

for file in files:
    data_frame[file.replace('.csv', '')] = pd.read_csv('data/' + file)

train = data_frame['train_users']
test = data_frame['test_users']
train = train.fillna(-1)
test = test.fillna(-1)

labels = train['country_destination'].values
print(labels)

print("Program finished")