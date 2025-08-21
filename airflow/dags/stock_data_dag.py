from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import importlib.util

# Force-load fetch_stock_data.py from /opt/airflow
spec = importlib.util.spec_from_file_location("fetch_stock_data", "/opt/airflow/fetch_stock_data.py")
fetch_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fetch_module)

# Assign the function so Airflow can use it
fetch_and_store = fetch_module.fetch_and_store

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="stock_data_pipeline",
    default_args=default_args,
    description="Fetch stock data and store in Postgres",
    schedule_interval="@daily",   # change to "@hourly" if you want more frequent
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    fetch_task = PythonOperator(
        task_id="fetch_and_store_stock",
        python_callable=fetch_and_store,
    )