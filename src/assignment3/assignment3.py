from airflow import DAG
from datetime import timedelta,datetime
from airflow.operators.python_operator import PythonOperator

default_args={
     'owner':"lakshmi",
      'retries':5,
     'retry_delay':timedelta(minutes=1)
}
def greet():
    print("welcome to the airflow")
dag= DAG(
    default_args=default_args,
    dag_id="our_fourth_id",
    description="this is the one of the most finest description",
    start_date=datetime(2024,4,1),
    schedule_interval='@daily'

)
task1=PythonOperator(
        task_id="first_id",
        python_callable=greet,
        dag=dag,
    )
task1
