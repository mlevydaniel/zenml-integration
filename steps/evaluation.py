import logging

import numpy as np
import pandas as pd
from model.evaluation import MSE, RMSE, R2Score
from sklearn.base import RegressorMixin

from typing import Tuple
from typing_extensions import Annotated

import mlflow
from zenml import step
from zenml.client import Client
from dotenv import load_dotenv

load_dotenv()

experiment_tracker = Client().active_stack.experiment_tracker

# @step
@step(experiment_tracker=experiment_tracker.name)
def evaluation(
    model: RegressorMixin,
    X_test: pd.DataFrame,
    y_test: pd.Series
) -> Tuple[
    Annotated[float, "r2_score"],
    Annotated[float, "rmse"]
]:
    """
    Evaluates the model performance based on the evaluation strategy.
    """
    # with mlflow.start_run(nested=True) as nested_run:
    try:
        y_pred = model.predict(X_test)
        mse = MSE().calculate_score(y_test, y_pred)
        mlflow.log_metric("mse", mse)

        rmse = RMSE().calculate_score(y_test, y_pred)
        mlflow.log_metric("rmse", rmse)

        r2_score = R2Score().calculate_score(y_test, y_pred)
        mlflow.log_metric("r2_score", r2_score)

        logging.info(f"MSE: {mse}, RMSE: {rmse}, R2 Score: {r2_score}")

        return r2_score, rmse

    except Exception as e:
        logging.exception(f"Error in evaluating model: {e}")
        raise e
