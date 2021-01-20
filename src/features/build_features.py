import numpy as np


def drop_columns(df, cols):
    """
    Drop the data frame columns.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe with columns to be dropped.
    cols: list of str
        List with column names.

    Returns
    -------
    pandas.DataFrame
        Dataframe with columns dropped.

    """
    return df.drop(cols, axis=1)


def replace_nan_inf(df):
    """
    Replace missing and infinity values with -999.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe with values to be replaced.

    Returns
    -------
    pandas.DataFrame
        Dataframe with missing and infinity values replaced with -999.

    """
    return df.replace(to_replace=[np.nan, np.inf, -np.inf],
                      value=-999)
