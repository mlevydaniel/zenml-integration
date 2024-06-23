import logging

import pandas as pd
from model.model_dev import (
    HyperparameterTuner,
    LightGBMModel,
    LinearRegressionModel,
    RandomForestModel,
    XGBoostModel,
)
from sklearn.base import RegressorMixin

import mlflow
from zenml import step
from zenml.client import Client

from .config import ModelNameConfig

from dotenv import load_dotenv

load_dotenv()

experiment_tracker = Client().active_stack.experiment_tracker

# @step(enable_cache=False)
@step(enable_cache=False, experiment_tracker=experiment_tracker.name)
def train_model(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
    config: ModelNameConfig
) -> RegressorMixin:

    """
    Trains model on the ingested data.

    Args:
        X_train: Training data
        X_test: Testing data
        y_train: Training target
        y_test: Testing target
    """

    # with mlflow.start_run(nested=True) as nested_run:
    try:
        model = None
        if config.model_name == "LinearRegression":
            mlflow.sklearn.autolog()
            model = LinearRegressionModel()
            trained_model = model.train(X_train, y_train)
            return trained_model

        elif config.model_name == "RandomForest":
            mlflow.sklearn.autolog()
            model = RandomForestModel()
            trained_model = model.train(X_train, y_train)
            return trained_model
        else:
            raise ValueError("Model {} not supported".format(config.model_name))
    except Exception as e:
        logging.exception("Error in training model: {}".format(e))
        raise e
