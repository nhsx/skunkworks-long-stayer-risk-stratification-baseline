import math
import numpy as np
from sklearn.metrics import mean_absolute_error, f1_score


def risk_score(los):
    """Return risk score (1-5) based on LoS

    Parameters:
        los (float): length of stay in days

    Returns:
        (int): risk score (1 = Very low risk, 5 = High risk)
    """

    # round los up to whole days
    los = math.ceil(los)

    if los > 15:
        return 5
    elif los > 13:
        return 4
    elif los > 10:
        return 3
    elif los > 6:
        return 2
    else:
        return 1


def train_model(gsc, X_train, y_train, evaluator):
    """Uses a GridSearchCV instance to find a reasonable model, and store
    performance and fitted model into a python dict

    Parameters:

        gsc (sklearn.model_selection.GridSearchCV object): defined model
        X_train (pandas dataframe): training dataframe with features
        y_train (pandas dataframe): training dataframe with targets
        evaluator (object): one of "mean_absolute_error" or "f1_weighted"

    Returns:

        (dict): resulting fitted model and performance metrics
    """

    grid_result = gsc.fit(X_train, y_train)

    # note model scoring approach defined in gsc
    model = {
        "cv_metric_mean": np.round(
            grid_result.cv_results_["mean_test_score"][grid_result.best_index_], 3
        ),
        "cv_metric_std": np.round(
            grid_result.cv_results_["std_test_score"][grid_result.best_index_], 2
        ),
        "model": grid_result.best_estimator_,
    }

    # retrain the best estimator on the full training set - note that refit=True
    # does not appear to do this
    model["model"].fit(X_train, y_train)

    # generate predictions, and make sure we remove any negative length of stay
    # predictions
    preds = np.clip(model["model"].predict(X_train), 0, None)

    # calculate final performance
    if evaluator == "mean_absolute_error":
        model["mae"] = np.round(mean_absolute_error(y_train, preds), 3)
    elif evaluator == "f1_weighted":
        model["f1_weighted"] = np.round(f1_score(y_train, preds, average="weighted"), 3)
    else:
        raise ValueError("Evaluator parameter incorrectly specified")

    return model
