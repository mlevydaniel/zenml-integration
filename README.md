## Set up Guide

This guide will walk you through setting up a virtual environment, configuring Docker Compose for MLflow and ZenML servers, and setting up ZenML from the virtual environment.


1.	Create and activate the virtual environment:

```bash
python3.10 -m venv venv
source bin/venv/activate
```

2.	Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create .env File with the following content:
```bash
MLFLOW_TRACKING_URI=http://<mlflow-server-url>:5050
ZENML_SERVER_URI=http://<zenml-server-url>:8080
UID=${UID}
GID=${GID}
MLFLOW_USER=<your-mlflow-username>
MLFLOW_PASSWORD=<your-mlflow-password>
```

# Set up Docker Compose

To create the MLflow and ZenML servers, we will use Docker containers connected to a MySQL database. This replicates a real-world setting. The next section will recreate the same setting in GCP.

1.	Build and start the Docker containers:

```bash
docker-compose build
docker-compose up -d
```

2.	To stop the Docker containers:

```bash
docker-compose down
```

## Set up Zenml from virtual environment

Once the Docker containers are up and running, if this is the first time you run Zenml remotely, you have to create a user and password, then log in and finally set up a new stack:

```bash
# Install ZenML MLflow integration:
zenml integration install mlflow -y
zenml integration install gcp -y

# Register the MLflow experiment tracker, model deployer and artifact store:
zenml experiment-tracker register mlflow_tracker_new --flavor=mlflow --tracking_uri=http://localhost:5050 --tracking_username=mlflow_user --tracking_password=SecurePassword
zenml model-deployer register mlflow_new --flavor=mlflow

zenml artifact-store register local_store --flavor=local --path=/mnt/zenml_store
or
zenml artifact-store register gs_store --flavor=gcp --path=gs://zenml-integration/zenml

# Register a new ZenML stack:
zenml stack register mlflow_stack_new -a gs_store -o default -d mlflow_new -e mlflow_tracker_new --set
```

In case you need to modify the current stack:

```sh
 zenml stack update mlflow_stack_new -a gs_store
```

## Reconnect and Assign Existing Stack

Every time you restart the Docker Compose setup, reconnect to the existing stack:

1. Log in to server

2. Connect to the remote server and set existing stack:
```bash
zenml connect --url http://localhost:8080
zenml stack set mlflow_stack_new
```

## Usage


## License

Information about the project’s license.

## Contact
