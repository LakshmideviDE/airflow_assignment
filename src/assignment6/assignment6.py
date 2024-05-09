from airflow.sensors.filesystem import FileSensor
from airflow import DAG
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=3),
}

with DAG(
        default_args=default_args,
        dag_id="sensor_demo",
        start_date=datetime(2024, 5, 8),
        catchup=False,
        schedule_interval='@daily'  # @daily is called presets,
) as dag:
    wait_for_file = FileSensor(
        task_id="wait_for_file",
        fs_conn_id='wait_for_file',  # Assuming this connection ID is properly configured
        filepath='C:\Users\Lakshmidevi\Downloads\employee_1 - Sheet1.csv',  # Make sure this path is correct
        mode='reschedule',
        poke_interval=30
    )

