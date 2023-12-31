from math import sqrt

import pandas as pd

"""
Cheat sheet for stats tests:

Chi-Square test  -  Used to test TWO CATEGORICAL types of data.
Pearson's R  -  Used to test TWO CONTINUOUS types of data.
Spearman's R  -  Used to test TWO CONTINUOUS types of data.
T-Test  -  Used to test ONE CONTINUOUS AND ONE CATEGORICAL type of data.
Mann-Whitney  -  Used to test ONE CONTINUOUS AND ONE CATEGORICAL type of data.

Parametric tests relies on statistical distributions in data.
Non-Parametric tests do not rely on any kind of distribution.
"""


def eval_p(p_value):  # create a function that checks p-value for a significant result.
    """This function simply takes in a p-value checks if it is greater than or less than alpha."""
    alpha = 0.05  # set confidence interval
    if p_value < alpha:
        print(f'There is a signifcant result. P-value was {round(p_value,2)}.')
    else:
        print(f'There is no signifcant result. P-value was {round(p_value,2)}.')


def eval_pearson_r(r_value):
    """This function will evaluate Pearson's R."""
    if r_value >= 0.90:
        print(f'There is a very high positive correlation. R-value was {round(r_value,3)}.')
    elif r_value >= 0.70:
        print(f'There is a high positive correlation. R-value was {round(r_value,3)}.')
    elif r_value >= 0.40:
        print(f'There is a moderate positive correlation. R-value was {round(r_value,3)}.')
    elif r_value >= 0.20:
        print(f'There is a low positive correlation. R-value was {round(r_value,3)}.')
    elif r_value > 0.00:
        print(f'There is a very slight positive correlation. R-value was {round(r_value,3)}.')
    elif r_value == 0.00:
        print(f'There is no correlation. R-value was {round(r_value,3)}.')
    elif r_value >= -0.20:
        print(f'There is a very slight negative correlation. R-value was {round(r_value,3)}.')
    elif r_value >= -0.40:
        print(f'There is a low negative correlation. R-value was {round(r_value,3)}.')
    elif r_value >= -0.70:
        print(f'There is a moderate negative correlation. R-value was {round(r_value,3)}.')
    elif r_value >= -0.90:
        print(f'There is a high negative correlation. R-value was {round(r_value,3)}.')
    else:
        print(f'There is a very high negative correlation. R-value was {round(r_value, 2)}.')


def check_pearson(r, p):
    """This function combines two other functions to check the results of a pearson's r test."""
    eval_pearson_r(r)
    eval_p(p)


def check_ttest(t, p, tails=1):
    """This function will accept the t, and p-value from a T-test and analyze it. It will accordingly divide the p-value
    by 2 if this is a one-tailed test."""
    alpha = 0.05
    if tails == 1:
        if p / 2 > alpha:
            print(f'There is no signifcant result. P-value was {round(p,2)}.')
        else:
            print(f'There is a signifcant result. P-value was {round(p, 2)}.')
    if tails == 2:
        if p > alpha:
            print(f'There is no signifcant result. P-value was {round(p,2)}.')
        else:
            print(f'There is a signifcant result. P-value was {round(p, 2)}.')
    if t > 0:
        print(f'T-value was greater than 0. With a value of {round(t,2)}.')
    else:
        print(f'T-value was less than 0. With a value of {round(t,2)}.')


def baseline(data, method='both'):
    """This function will create a baseline. It accepts a dataframe and then returns one or two baseline models."""
    df = pd.DataFrame(data)  # Creates a copy of dataframe

    if method == 'mean':  # Creates a baseline model using mean()
        df['baseline'] = data.mean()
        return df
    elif method == 'median':  # Creates a baseline model using median()
        df['baseline'] = data.median()
        return df
    elif method == 'both':  # Creates a baseline model using both
        df['base_median'] = data.median()
        df['base_mean'] = data.mean()
        return df  # Returns dataframe with the baseline models


def eval_model(actual, model):
    """This function will accept two series of the model and actual data and calculate the metrics for the model."""
    residuals = model - actual  # Calculate residuals
    SSE = (residuals ** 2).sum()
    MSE = SSE / len(actual)
    RMSE = sqrt(MSE)
    return SSE, MSE, RMSE  # Returns the calculated metrics


def train_model(model, X_train, y_train, X_val, y_val):
    """This function accepts a model object, and the x and y train and validate dataframes. It will fit, predict, and
    evaluate the models on train and validate."""
    model.fit(X_train, y_train)  # Fits the model to the train data
    train_preds = model.predict(X_train)  # Create predictions for train
    skip, skip2, train_rmse = eval_model(y_train, train_preds)  # Caculate RMSE for model on train
    val_preds = model.predict(X_val)  # Creates predictions for validate
    skip3, skip4, val_rmse = eval_model(y_val, val_preds)  # Caculate RMSE for model on validate
    print(f'The train RMSE is {train_rmse}.')
    print(f'The validate RMSE is {val_rmse}.')
