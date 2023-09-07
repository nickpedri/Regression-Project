import pandas as pd
import numpy as np


def prep_zillow(df):

    """ This function will take in the zillow dataset and prepare it by renaming the columns, binning some of the
    data and removing some of the outliers from the dataset."""

    zil = df.copy()
    rename = {'bedroomcnt': 'bedrooms',  # Create a dictionary for new column names
              'bathroomcnt': 'bathrooms',
              'calculatedfinishedsquarefeet': 'sq_ft',
              'taxvaluedollarcnt': 'price'}
    zil = zil.rename(columns=rename)  # Rename colums using dictionary
    bed_bins = pd.cut(zil.bedrooms, bins=[-0.5, .5, 1.5, 2.5, 3.5, 4.5, 5.5, 1000],
                      labels=['0', '1', '2', '3', '4', '5', '6+'])
    zil.bedrooms = bed_bins
    new_baths = np.where(zil.bathrooms > 5, '6+', zil.bathrooms.astype(str))
    zil.bathrooms = new_baths
    zil = zil[zil.price < 2_500_000]
    return zil  # Return zil dataframe
