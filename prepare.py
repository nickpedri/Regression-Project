import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler


def prep_zillow(df, mvp=True):

    """ This function will take in the zillow dataset and prepare it by renaming the columns, binning some of the
    data and removing some of the outliers from the dataset."""

    if mvp:
        zil = df.copy()
        rename = {'bedroomcnt': 'bedrooms',  # Create a dictionary for new column names
                  'bathroomcnt': 'bathrooms',
                  'calculatedfinishedsquarefeet': 'sq_ft',
                  'taxvaluedollarcnt': 'price'}
        zil = zil.rename(columns=rename)  # Rename colums using dictionary
        bed_bins = pd.cut(zil.bedrooms, bins=[-0.5, .5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 1000],
                          labels=[0, 1, 2, 3, 4, 5, 6, 7])
        zil.bedrooms = bed_bins.astype(int)
        new_baths = np.where(zil.bathrooms > 6, 7, zil.bathrooms)
        zil.bathrooms = new_baths
        zil = zil[zil.sq_ft < 8_000]
        return zil  # Return zil dataframe
    if not mvp:
        zil = df.copy()
        rename = {'bedroomcnt': 'bedrooms',  # Create a dictionary for new column names
                  'bathroomcnt': 'bathrooms',
                  'calculatedfinishedsquarefeet': 'sq_ft',
                  'taxvaluedollarcnt': 'price'}
        zil = zil.rename(columns=rename)  # Rename colums using dictionary
        bed_bins = pd.cut(zil.bedrooms, bins=[-0.5, .5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 1000],
                          labels=[0, 1, 2, 3, 4, 5, 6, 7])
        zil.bedrooms = bed_bins.astype(int)
        new_baths = np.where(zil.bathrooms > 6, 7, zil.bathrooms)
        zil.bathrooms = new_baths
        zil = zil[zil.sq_ft < 8_000]
        return zil  # Return zil dataframe


def train_val_test(df, strat='None', seed=100, stratify=False):  # Splits dataframe into train, val, test
    """ This function will split my data into train, validate and test. It has the option to stratify."""
    if stratify:  # Will split with stratify if stratify is True
        train, val_test = train_test_split(df, train_size=0.7, random_state=seed, stratify=df[strat])
        val, test = train_test_split(val_test, train_size=0.5, random_state=seed, stratify=val_test[strat])
        return train, val, test
    if not stratify:  # Will split without stratify if stratify is False
        train, val_test = train_test_split(df, train_size=0.7, random_state=seed)
        val, test = train_test_split(val_test, train_size=0.5, random_state=seed)
        return train, val, test


def scale(df='?', train=None, val=None, test=None, method='mms', scaled_cols=None):
    if train is None or val is None or test is None:
        train, val, test = train_val_test(df)
    if scaled_cols is None:
        scaled_cols = ['sq_ft']
    if method == 'mms':
        mms = MinMaxScaler()
        mms.fit(train[scaled_cols])
        train[scaled_cols] = mms.transform(train[scaled_cols])
        val[scaled_cols] = mms.transform(val[scaled_cols])
        test[scaled_cols] = mms.transform(test[scaled_cols])
        return train, val, test
    if method == 'ss':
        ss = StandardScaler()
        ss.fit(train[scaled_cols])
        train[scaled_cols] = ss.transform(train[scaled_cols])
        val[scaled_cols] = ss.transform(val[scaled_cols])
        test[scaled_cols] = ss.transform(test[scaled_cols])
        return train, val, test
    if method == 'rs':
        rs = RobustScaler()
        rs.fit(train[scaled_cols])
        train[scaled_cols] = rs.transform(train[scaled_cols])
        val[scaled_cols] = rs.transform(val[scaled_cols])
        test[scaled_cols] = rs.transform(test[scaled_cols])
        return train, val, test


def split_xy(df, target=''):
    x_df = df.drop(columns=target)
    y_df = df[target]
    return x_df, y_df
