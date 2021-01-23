import numpy as np
import pandas as pd


def replace_nan_inf(df, value=None):
    """
    Replace missing and infinity values.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe with values to be replaced.

    value : int, float
        Value to replace any missing or numpy.inf values. Defaults to numpy.nan
    Returns
    -------
    pandas.DataFrame
        Dataframe with missing and infinity values replaced with -999.

    """
    if value is None:
        value = np.nan
    return df.replace(to_replace=[np.nan, np.inf, -np.inf],
                      value=value)


def shift_concat(df, periods=1, fill_value=None):
    """
    Build dataframe of shifted index.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe with columns to be shifted.
    periods : int
        Number of periods to shift. Should be positive.
    fill_value : object, optional
        The scalar value to use for newly introduced missing values. Defaults
        to numpy.nan.

    Returns
    -------
    pandas.DataFrame
        Shifted dataframes concatenated along columns axis.

    Notes
    -------
    Based on Paulo Bestagini's augment_features_window from SEG 2016 ML
    competition.
    https://github.com/seg/2016-ml-contest/blob/master/ispl/facies_classification_try01.ipynb

    Example
    -------
    Shift df by one period and concatenate.

    >>> df = pd.DataFrame({'gr': [1.1, 2.1], 'den': [2.1, 2.2]})
    >>> shift_concat(df)
        gr_shifted_1  den_shifted_1  gr   den  gr_shifted_-1   den_shifted_-1
    0      NaN            NaN        1.1  2.1      2.1             2.2
    1      1.1            2.1        2.1  2.2      NaN             NaN

    """
    if fill_value is None:
        fill_value = np.nan

    dfs = []
    for period in range(periods, -1*periods - 1, -1):

        if period == 0:
            dfs.append(df)
            continue

        df_shifted = df.shift(period, fill_value=fill_value)

        df_shifted.columns = [f'{col}_shifted_{str(period)}'
                              for col in df_shifted.columns]

        dfs.append(df_shifted)

    return pd.concat(dfs, axis=1)


def gradient(df, depth_col):
    """
    Calculate the gradient for all features along the provided `depth_col`
    column.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe with columns to be used in the gradient calculation.
    depth_col : str
        Dataframe column name to be used as depth reference.

    Returns
    -------
    pandas.DataFrame
        Gradient of `df` along `depth_col` column. The depth column is not in
        the output dataframe.

    Notes
    -------
    Based on Paulo Bestagini's augment_features_window from SEG 2016 ML
    competition.
    https://github.com/seg/2016-ml-contest/blob/master/ispl/facies_classification_try01.ipynb

    Example
    -------
    Calculate gradient of columns along `md`.

    >>> df = pd.DataFrame({'gr': [100.1, 100.2, 100.3],
                          'den': [2.1, 2.2, 2.3],
                          'md': [500, 500.5, 501]})
    >>> gradient(df, 'md')
        gr  den
    0  NaN  NaN
    1  0.2  0.2
    2  0.2  0.2

    """
    depth_diff = df[depth_col].diff()

    denom_zeros = np.isclose(depth_diff, 0)
    depth_diff[denom_zeros] = 0.001

    df_diff = df.drop(depth_col, axis=1)
    df_diff = df_diff.diff()

    # Add suffix to column names
    df_diff.columns = [f'{col}_gradient' for col in df_diff.columns]

    return df_diff.divide(depth_diff, axis=0)


def shift_concat_gradient(df, depth_col, well_col, periods=1, fill_value=None):
    """
    Augment features using `shif_concat` and `gradient`.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataframe with columns to be augmented.
    depth_col : str
        Dataframe column name to be used as depth reference.
    well_col : str
        Dataframe column name to be used as well reference.
    periods : int
        Number of periods to shift. Should be positive.
    fill_value : object, optional
        The scalar value to use for newly introduced missing values. Defaults
        to numpy.nan.

    Returns
    -------
    pandas.DataFrame
        Augmented dataframe.

    Notes
    -------
    Based on Paulo Bestagini's augment_features_window from SEG 2016 ML
    competition.
    https://github.com/seg/2016-ml-contest/blob/master/ispl/facies_classification_try01.ipynb

    Example
    -------
    Augment features of `df` by shifting and taking the gradient.

    >>> df = pd.DataFrame({'gr': [100.1, 100.2, 100.3, 20.1, 20.2, 20.3],
                          'den': [2.1, 2.2, 2.3, 1.7, 1.8, 1.9],
                           'md': [500, 500.5, 501, 1000, 1000.05, 1001],
                         'well': [1, 1, 1, 2, 2, 2]})
    >>> shift_concat_gradient(df, 'md', 'well', periods=1, fill_value=None)
        gr_shifted_1  den_shifted_1     gr    den  ...  well   md    gr_gradient  den_gradient
    0         NaN          NaN         100.1  2.1  ...   1   500.00        NaN           NaN
    1       100.1          2.1         100.2  2.2  ...   1   500.50   0.200000      0.200000
    2       100.2          2.2         100.3  2.3  ...   1   501.00   0.200000      0.200000
    3         NaN          NaN          20.1  1.7  ...   2  1000.00        NaN           NaN
    4        20.1          1.7          20.2  1.8  ...   2  1000.05   2.000000      2.000000
    5        20.2          1.8          20.3  1.9  ...   2  1001.00   0.105263      0.105263

    """
    # TODO 'Consider filling missing values created here with DataFrame.fillna'

    # Gradient should only be applied to float columns
    float_columns = df.select_dtypes(include='float').columns

    # Don't shift depth
    depth = df.loc[:, depth_col]

    grouped = df.groupby(well_col, sort=False)

    df_aug_groups = []
    for name, group in grouped:
        shift_cols_df = group.drop([well_col, depth_col], axis=1)

        group_shift = shift_concat(shift_cols_df,
                                   periods=periods,
                                   fill_value=fill_value)

        # Add back the well name and depth
        group_shift[well_col] = name
        group_shift[depth_col] = depth

        group_gradient = group.loc[:, float_columns]

        group_gradient = gradient(group_gradient, depth_col)

        group_aug = pd.concat([group_shift, group_gradient], axis=1)

        df_aug_groups.append(group_aug)

    return pd.concat(df_aug_groups)
