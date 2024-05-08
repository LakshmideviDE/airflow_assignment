from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args={
    'owner':'lakshmi',
     'retries':5,
      'retry_delay':timedelta(minutes=2)
}
with DAG (
    dag_id='our_first_dag',
    default_args=default_args,
    description='this is the first dag that we should write',
    schedule_interval='@daily',
    start_date=datetime(2024,6,26)
    )as dag:
    task1=BashOperator(
        task_id='first_task',
        bash_command="echo hello world"
    )
task1 






























