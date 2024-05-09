from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'lakshmi',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}
def simple():
    print("hello airflow")

    dag_a=DAG(
        dag_id='our_third_dag',
        default_args=default_args,
        schedule_interval='@daily',
        start_date=datetime(2024, 5, 4, 2)
    )

    task1 = PythonOperator(
        task_id='first_task',
        python_callable=simple,
        dag=dag_a
    )
    task2 = PythonOperator(
        task_id='second_task',
        python_callable=simple,
        dag=dag_a
    )
    task1 >> task2
