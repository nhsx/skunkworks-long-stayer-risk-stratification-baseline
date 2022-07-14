import math
import numpy as np
from sklearn.metrics import f1_score, mean_squared_error


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


def train_and_test_model(estimator, X_train, y_train, X_test, y_test, scoring_metric):
    """Trains and tests a model, returning results in a python dict

    Parameters:

        estimator (object): estimator object implementing 'fit'
        X_train (pandas dataframe): training dataframe with features
        y_train (pandas dataframe): training dataframe with targets
        X_test (pandas dataframe): test dataframe with features
        y_test (pandas dataframe): test dataframe with targets
        scoring_metric (object): one of "rmse" or "f1_weighted"


    Returns:

        (dict): resulting fitted model and performance metrics
    """

    model = {}

    # fit the model based on the training data
    model["model"] = estimator.fit(X_train, y_train)

    # generate predictions of the training set
    preds_train = np.clip(model["model"].predict(X_train), 0, None)
    preds_test = np.clip(model["model"].predict(X_test), 0, None)

    # calculate performance
    if scoring_metric == "rmse":
        model["train_metric"] = mean_squared_error(y_train, preds_train, squared=False)
        model["test_metric"] = mean_squared_error(y_test, preds_test, squared=False)
    elif scoring_metric == "f1_weighted":
        model["train_metric"] = f1_score(y_train, preds_train, average="weighted")
        model["test_metric"] = f1_score(y_test, preds_test, average="weighted")
    else:
        raise ValueError("Scoring metric incorrectly specified")

    model["scoring_metric"] = scoring_metric

    return model
