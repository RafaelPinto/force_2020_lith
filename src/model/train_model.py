import numpy as np

from sklearn.metrics import accuracy_score, f1_score

from src.definitions import ROOT_DIR


def score(y_true, y_pred):
    """
    Competition scoring function.

    Parameters
    ----------
    y_true : pandas.Series
        Ground truth (correct) target values.
    y_pred: pandas.Series
        Estimated targets as returned by a classifier.

    Returns
    ----------
    float
        2020 FORCE ML lithology competition custome score.

    """
    scoring_matrix_path = ROOT_DIR / 'data/external/penalty_matrix.npy'
    scoring_matrix = np.load(scoring_matrix_path)

    S = 0.0

    for true_val, pred_val in zip(y_true, y_pred):
        S -= scoring_matrix[true_val, pred_val]

    return S/y_true.shape[0]


def show_evaluation(y_true, y_pred):
    """
    Print model performance and evaluation.

    Parameters
    ----------
    y_true : pandas.Series
        Ground truth (correct) target values.
    y_pred: pandas.Series
        Estimated targets as returned by a classifier.

    """
    print(f'Competition score: {score(y_true, y_pred)}')
    print(f'Accuracy: {accuracy_score(y_true, y_pred)}')
    print(f'F1: {f1_score(y_true, y_pred, average="weighted")}')
