import numpy as np

from src.definitions import ROOT_DIR


def score(y_true, y_pred):
    """
    Competition scoring function.

    """
    scoring_matrix_path = ROOT_DIR / 'data/external/penalty_matrix.npy'
    scoring_matrix = np.load(scoring_matrix_path)

    S = 0.0
    y_true = y_true.astype(int)
    y_pred = y_pred.astype(int)

    for i in range(0, y_true.shape[0]):
        S -= scoring_matrix[y_true[i], y_pred[i]]

    return S/y_true.shape[0]
