import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.impute import SimpleImputer


def prep_zillow(df, mvp=True, new_fips=True):

    """ This function will take in the zillow dataset and prepare it by renaming the columns, binning some of the
    data and removing some of the outliers from the dataset. There are two options for a simple dataframe and one with
    more features."""

    if mvp:  # Cleans up the simple MVP dataframe
        zil = df.copy()

        rename = {'bedroomcnt': 'bedrooms',  # Create a dictionary for new column names
                  'bathroomcnt': 'bathrooms',
                  'calculatedfinishedsquarefeet': 'sq_ft',
                  'taxvaluedollarcnt': 'price'}
        zil = zil.rename(columns=rename)  # Rename colums using dictionary

        bed_bins = pd.cut(zil.bedrooms, bins=[-0.5, .5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 1000],
                          labels=[0, 1, 2, 3, 4, 5, 6, 7])
        zil.bedrooms = bed_bins.astype(int)

        new_baths = np.where(zil.bathrooms > 6, 7, zil.bathrooms)  # Bins houses with numerous bathrooms into one group
        zil.bathrooms = new_baths

        zil = zil[zil.sq_ft < 4_000]  # Removes houses with sq ft higher than 4,000

        return zil  # Return zil dataframe

    if not mvp:  # Cleans up the bigger more complex dataframe

        zil = df.copy()  # Create copy of dataframe

        imputer = SimpleImputer(strategy='constant', fill_value=0)
        imputer.fit(zil[['poolcnt']])
        zil['poolcnt'] = imputer.transform(zil[['poolcnt']])
        imputer.fit(zil[['garagecarcnt']])
        zil['garagecarcnt'] = imputer.transform(zil[['garagecarcnt']])
        imputer.fit(zil[['fireplacecnt']])
        zil['fireplacecnt'] = imputer.transform(zil[['fireplacecnt']])
        # Impute all missing values with 0 since they are essentially representing 0

        zil = zil.dropna()  # Drop the rest of the nulls

        rename = {'bedroomcnt': 'bedrooms', 'bathroomcnt': 'bathrooms', 'calculatedfinishedsquarefeet': 'sq_ft',
                  'poolcnt': 'pools', 'garagecarcnt': 'garages', 'fireplacecnt': 'fireplaces', 'yearbuilt': 'year',
                  'lotsizesquarefeet': 'lot_sq_ft', 'taxvaluedollarcnt': 'price'}
        zil = zil.rename(columns=rename)  # Rename colums using dictionary

        bed_bins = pd.cut(zil.bedrooms, bins=[-0.5, .5, 1.5, 2.5, 3.5, 4.5, 5.5, 10000],
                          labels=[0, 1, 2, 3, 4, 5, 6])
        zil.bedrooms = bed_bins.astype(int)  # Bin bedrooms

        new_baths = np.where(zil.bathrooms >= 5, 5, zil.bathrooms)
        zil.bathrooms = new_baths  # Bin bathrooms

        zil = zil[zil.sq_ft < 4_000]  # Removes houses with sq ft higher than 4,000

        if new_fips:
            fips_codes = {'6037': 'Los Angeles County',
                          '6059': 'Orange County',
                          '6111': 'Ventura County'}
            zil.fips = [fips_codes.get(fip) for fip in zil.fips.astype(int).astype(str)]
            # Replace fips codes with actual county names.

        zil.pools = zil.pools.astype(int)  # Convert pool dtype to int

        zil.garages = zil.garages.astype(int)
        new_garages = np.where(zil.garages >= 3, 3, zil.garages)
        zil.garages = new_garages  # Bin garages

        zil.fireplaces = zil.fireplaces.astype(int)
        new_fireplaces = np.where(zil.fireplaces >= 3, 3, zil.fireplaces)
        zil.fireplaces = new_fireplaces  # Bin fireplaces

        zil.year = zil.year.astype(int)  # Convert year to int

        zil = zil[zil.lot_sq_ft < 20_000]  # Remove houses with lot sizes bigger than 20,000 sq ft

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
    """This function will take in a dataframe or the train, val, test dataframes and scale the data according to
    whatever method is chosen."""
    if train is None or val is None or test is None:
        train, val, test = train_val_test(df)
    if scaled_cols is None:
        scaled_cols = ['bedrooms', 'bathrooms', 'sq_ft', 'year', 'lot_sq_ft']
    if method == 'mms':  # MinMax is chosen
        mms = MinMaxScaler()
        mms.fit(train[scaled_cols])
        train[scaled_cols] = mms.transform(train[scaled_cols])
        val[scaled_cols] = mms.transform(val[scaled_cols])
        test[scaled_cols] = mms.transform(test[scaled_cols])
        return train, val, test
    if method == 'ss':  # Standard is chosen
        ss = StandardScaler()
        ss.fit(train[scaled_cols])
        train[scaled_cols] = ss.transform(train[scaled_cols])
        val[scaled_cols] = ss.transform(val[scaled_cols])
        test[scaled_cols] = ss.transform(test[scaled_cols])
        return train, val, test
    if method == 'rs':  # Robust is chosen
        rs = RobustScaler()
        rs.fit(train[scaled_cols])
        train[scaled_cols] = rs.transform(train[scaled_cols])
        val[scaled_cols] = rs.transform(val[scaled_cols])
        test[scaled_cols] = rs.transform(test[scaled_cols])
        return train, val, test  # returns train test and val


def split_xy(df, target=''):
    """This function will split x and y according to the target variable."""
    x_df = df.drop(columns=target)
    y_df = df[target]
    return x_df, y_df  # Returns dataframe


def dummies(train, val, test, drop_first, normal_list):
    """This function will one hot encode a dataframe. It accepts one or more dataframes, and two lists of columns."""

    train = pd.get_dummies(train, columns=drop_first)  # Drops first value from this list of columns
    train = pd.get_dummies(train, columns=normal_list)  # Does not drop first from this list of columns

    val = pd.get_dummies(val, columns=drop_first)
    val = pd.get_dummies(val, columns=normal_list)

    test = pd.get_dummies(test, columns=drop_first)
    test = pd.get_dummies(test, columns=normal_list)

    return train, val, test  # Returns encoded dataframes
