from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2021, 6, 26)
}
dag1 = DAG(
    default_args=default_args,
    description='This is the first DAG',
    dag_id='first',
    start_date=datetime(2023, 6, 26),
    schedule_interval='@monthly'
)

task1 = BashOperator(
    task_id="first_mul",
    bash_command="echo first operator",
    dag=dag1
)
def lakshmi():
    print("Downloading")

# Define the second DAG
dag2 = DAG(
    default_args=default_args,
    description='This is the second DAG',
    dag_id='second',
    start_date=datetime(2020, 10, 17),
    schedule_interval='@daily'
)

task2 = PythonOperator(
    task_id='downloading',
    python_callable=lakshmi,
    dag=dag2
)

trigger_dag2 = TriggerDagRunOperator(
    task_id='trigger_dag2',
    trigger_dag_id='second',
    reset_dag_run=True,
    dag=dag1,
)
trigger_dag2

