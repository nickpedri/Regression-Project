from math import sqrt

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
    if r_value > 0.90:
        print(f'There is a very high positive correlation. R-value was {round(r_value,2)}.')
    elif r_value > 0.70:
        print(f'There is a high positive correlation. R-value was {round(r_value,2)}.')
    elif r_value > 0.50:
        print(f'There is a moderate positive correlation. R-value was {round(r_value,2)}.')
    elif r_value > 0.25:
        print(f'There is a low positive correlation. R-value was {round(r_value,2)}.')
    elif r_value > 0.00:
        print(f'There is a very slight positive correlation. R-value was {round(r_value,2)}.')
    elif r_value > -0.25:
        print(f'There is a very slight negative correlation. R-value was {round(r_value,2)}.')
    elif r_value > -0.50:
        print(f'There is a low negative correlation. R-value was {round(r_value,2)}.')
    elif r_value > -0.70:
        print(f'There is a moderate negative correlation. R-value was {round(r_value,2)}.')
    elif r_value > -0.90:
        print(f'There is a high negative correlation. R-value was {round(r_value,2)}.')
    else:
        print(f'There is a very high negative correlation. R-value was {round(r_value, 2)}.')


def check_pearson(r, p):
    """This function combines two other functions to check the results of a pearson's r test."""
    eval_pearson_r(r)
    eval_p(p)


def check_ttest(t, p, tails=1):
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


def baseline(data, actual='', method='both'):
    df = data.copy()
    if method == 'mean':
        df['baseline'] = df[actual].mean()
        return df
    elif method == 'median':
        df['baseline'] = df[actual].median()
        return df
    elif method == 'both':
        df['base_median'] = df[actual].median()
        df['base_mean'] = df[actual].mean()
        return df


def eval_model(actual, model):
    residuals = model - actual
    SSE = (residuals ** 2).sum()
    MSE = SSE / len(actual)
    RMSE = sqrt(MSE)
    return SSE, MSE, RMSE


def train_model(model, X_train, y_train, X_val, y_val):
    model.fit(X_train, y_train)
    train_preds = model.predict(X_train)
    skip, skip2, train_rmse = eval_model(y_train, train_preds)
    val_preds = model.predict(X_val)
    skip3, skip4, val_rmse = eval_model(y_val, val_preds)
    print(f'The train RMSE is {train_rmse}.')
    print(f'The validate RMSE is {val_rmse}.')
