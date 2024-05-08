from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

# Define Python functions for tasks
def task1():
    print("This is the first task that was created")

def task2():
    print("This is the second task for demo dag")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 6, 26),
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}
with DAG(
    'demo_dag',
    default_args=default_args,
    description='A simple demo DAG',
    schedule_interval=timedelta(days=1),
) as dag:
    # Define tasks
    task_1 = PythonOperator(
        task_id='first_task',
        python_callable=task1,
    )
    task_2 = PythonOperator(
        task_id='second_task',
        python_callable=task2,
    )
    task1 >> task2
