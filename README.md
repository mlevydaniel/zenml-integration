```bash
zenml integration install mlflow -y
zenml experiment-tracker register mlflow_tracker_new --flavor=mlflow
zenml model-deployer register mlflow_new --flavor=mlflow
zenml stack register mlflow_stack_new -a default -o default -d mlflow_new -e mlflow_tracker_new --set
```

```bash
docker-compose build
docker-compose up -d
zenml connect --url http://localhost:8080
docker-compose down
```