from pipelines.training_pipeline import train_pipeline
from zenml.client import Client
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


if __name__ == "__main__":

    # Check Zenml integration with MLflow
    print(Client().active_stack.experiment_tracker.get_tracking_uri())

    training = train_pipeline()
    training.run()
