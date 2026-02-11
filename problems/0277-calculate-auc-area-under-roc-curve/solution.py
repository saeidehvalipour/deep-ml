import numpy as np

def calculate_auc(y_true, y_scores):
    """
    ROC-AUC via ROC points (FPR, TPR) computed at score thresholds,
    then trapezoid integration.

    - Handles ties correctly by updating counts in batches for each unique score.
    - Returns 0.0 if all labels are the same class.
    """
    y_true = np.asarray(y_true, dtype=int)
    y_scores = np.asarray(y_scores, dtype=float)

    if y_true.size == 0:
        return 0.0

    P = int((y_true == 1).sum())
    N = int((y_true == 0).sum())

    # Edge case: AUC undefined if only one class exists
    if P == 0 or N == 0:
        return 0.0

    # Sort by score descending
    order = np.argsort(-y_scores)
    scores_sorted = y_scores[order]
    y_sorted = y_true[order]

    # Start at threshold above max score: no predicted positives
    tp = 0
    fp = 0
    roc_points = [(0.0, 0.0)]  # (FPR, TPR)

    i = 0
    n = len(y_sorted)

    # Process in groups of equal scores (ties)
    while i < n:
        j = i
        whil