import pandas as pd
import os
from env import get_connection


def sql_query(db='None', query='None'):

    """This is a function to easily and quickly create a SQL query in python without having to perform multiple steps.
     This function takes in two arguments: db which is the database that you wish to connect/use, and query which is the
    query that you would like to run."""

    if db == 'None':
        print('Database not specified.')
    elif query == 'None':
        print('No query!')
    else:
        db_url = get_connection(db)
        df = pd.read_sql(query, db_url)
        return df


def zillow_data(advanced=False):

    """ This function pulls zillow data from the CodeUp server database or from a local .csv file. The function will
    either load an existing local .csv file if it exists, or it will create a SQL query to pull the data and then save
    it to a local .csv file for next time. Has two options for a simple table or advanced."""

    if advanced is False:
        filename = 'zillow.csv'  # Checks for local file
        if os.path.isfile(filename):
            return pd.read_csv(filename)  # Returns local file if there is one
        else:
            query = '''SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt 
           FROM properties_2017 JOIN predictions_2017 USING(id)
           WHERE SUBSTR(transactiondate, 1, 4) = 2017 AND propertylandusetypeid = 261'''  # SQL query

            url = get_connection('zillow')  # Creates url to connect to server
            df = pd.read_sql(query, url)  # Queries data
            df = df.dropna()
            df.to_csv(filename, index=False)  # Saves data locally
            return df  # returns queried data

    if advanced:  # will create and pull a way more complex table
        filename = 'zillow_advanced.csv'  # Checks for local file
        if os.path.isfile(filename):
            return pd.read_csv(filename)  # Returns local file if there is one
        else:
            query = '''SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, poolcnt, 
            garagecarcnt, fireplacecnt, fips, yearbuilt, lotsizesquarefeet
            FROM properties_2017 JOIN predictions_2017 USING(id)
            WHERE SUBSTR(transactiondate, 1, 4) = 2017 AND propertylandusetypeid = 261'''  # SQL query'''  # SQL query
            url = get_connection('zillow')  # Creates url to connect to server
            df = pd.read_sql(query, url)  # Queries data
            # df = df.dropna()
            # df.to_csv(filename, index=False)  # Saves data locally
            return df  # returns queried data

