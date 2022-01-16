import pandas as pd
import numpy as np
import pandas
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation


def missing_values_table(df):
    # Total missing values
    mis_val = df.isnull().sum()
    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)
    # Make a table with the results
    mis_val_table = pandas.concat([mis_val, mis_val_percent], axis=1)
    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values'})
    # Sort the table by percentage of missing descending
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:, 1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
    # Print some summary information
    # Return the dataframe with missing information
    return mis_val_table_ren_columns


pd.set_option('display.max_columns', 200)
seaborn_plotmaker = sns.load_dataset("flights")
sns.set(color_codes=True)
df = pd.read_csv("ramen-ratings.csv")
df.replace({'Not Available': np.nan})
# To display the top 5 rows
duplicate_rows_df = df[df.duplicated()]
df = df.drop_duplicates()
print(df.shape)
print('====')
for i in list(df.columns):
    print(i)
print('====')
dftf = missing_values_table(df)
for index in list(dftf.index):
    if dftf.at[index, '% of Total Values'] > 50.0:
        df = df.drop(index, axis=1)
df = df.dropna()
print('====')
for i in list(df.columns):
    print(i)
print('====')
print(df.shape)
print(df.dtypes)
b_corr = []
d_cori = {}
print('corr', df.corr())
for i in list(df.corr()['Review #'].index):
    b_corr.append(df.corr()['Review #'][i])
    d_cori[df.corr()['Review #'][i]] = i
print(*b_corr)
for i in d_cori.keys():
    print(d_cori[i])