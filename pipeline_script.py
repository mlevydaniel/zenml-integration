from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now you can access the environment variables
mlflow_tracking_uri = os.getenv('MLFLOW_TRACKING_URI')
zenml_server_uri = os.getenv('ZENML_SERVER_URI')

# Import necessary modules
from zenml.pipelines import pipeline
from zenml.steps import step
import mlflow

@step
def import_data():
    # Your data import logic
    pass

@step
def train_model(data):
    with mlflow.start_run():
        # Your model training logic
        mlflow.log_param("param2", "value2")
        mlflow.log_metric("metric2", 0.9)

@pipeline
def my_pipeline(import_data, train_model):
    data = import_data()
    train_model(data)

# Instantiate and run the pipeline
pipe = my_pipeline(
    import_data=import_data(),
    train_model=train_model()
)
pipe.run()
