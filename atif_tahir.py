import pandas as pd


# Load the data into DataFrames
airbnb_df  = pd.read_csv('train_users_2.csv')
test_df    = pd.read_csv('test_users.csv')
gender_df = pd.read_csv('age_gender_bkts.csv')
sessions_df = pd.read_csv('sessions.csv')
countries_df = pd.read_csv('countries.csv')

print (airbnb_df.head())
print (test_df.head())

# Merge train and test users
users = pd.concat((airbnb_df, test_df), axis=0, ignore_index=True)

print (users.head())

print('intital extraction done')

