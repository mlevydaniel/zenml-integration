from pipelines.training_pipeline import train_pipeline
from zenml.client import Client
from dotenv import load_dotenv
import os
import mlflow


# Load environment variables from .env file
load_dotenv()


if __name__ == "__main__":

    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    training = train_pipeline()
    training.run()

    # # Load environment variable for MLflow tracking URI
    # mlflow_tracking_uri = os.getenv('MLFLOW_TRACKING_URI')
    # if mlflow_tracking_uri is None:
    #     raise ValueError("MLFLOW_TRACKING_URI environment variable not set")

    # mlflow.set_tracking_uri(mlflow_tracking_uri)
    # mlflow.set_experiment("test-mlflow")

    # with mlflow.start_run() as run:
    #     mlflow.set_tags({"mlflow.parentRunId": run.info.run_id})
    #     training = train_pipeline()
    #     training.run()
