import pandas as pd

df_train = pd.read_csv('/Users/ky/Desktop/depression-detect/raw_data/labels/train_split_Depression_AVEC2017.csv')

df_test = pd.read_csv('/Users/ky/Desktop/depression-detect/raw_data/labels/dev_split_Depression_AVEC2017.csv')

df_holdout = pd.read_csv('/Users/ky/Desktop/depression-detect/raw_data/labels/dev_split_Depression_AVEC2017.csv')
