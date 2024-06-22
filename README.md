## Set up Virtual Machine

```bash
python3.10 -m venv venv
source bin/venv/activate
pip install -r requirements.txt
```

# Set up Docker Compose

```bash
docker-compose build
docker-compose up -d
docker-compose down
```

## Set up Zenml from virtual environment

```bash
zenml connect --url http://localhost:8080
zenml integration install mlflow -y
zenml experiment-tracker register mlflow_tracker_new --flavor=mlflow
zenml model-deployer register mlflow_new --flavor=mlflow
zenml stack register mlflow_stack_new -a default -o default -d mlflow_new -e mlflow_tracker_new --set
```

# Every time we turn on the Docker compose we need to reconnect and assign the existing stack

1. Log in to server

2. Connect and set existing stack:
```bash
zenml connect --url http://localhost:8080
zenml stack set mlflow_stack_new
```