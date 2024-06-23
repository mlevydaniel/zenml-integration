from zenml.config import DockerSettings
from zenml.integrations.constants import MLFLOW
from zenml.pipelines import pipeline

from steps.ingest_data import ingest_data
from steps.clean_data import clean_data
from steps.model_train import train_model
from steps.evaluation import evaluation

docker_settings = DockerSettings(required_integrations=[MLFLOW])


@pipeline(enable_cache=False)
def train_pipeline():
    df = ingest_data()
    X_train, X_test, y_train, y_test = clean_data(df)
    model = train_model(X_train, X_test, y_train, y_test)
    r2_score, rmse = evaluation(model, X_test, y_test)
