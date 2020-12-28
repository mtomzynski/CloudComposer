import datetime

import airflow
from airflow.operators import bash_operator

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)

default_args = {
    'owner': 'Composer Exxample',
    'depends_on_past': False,
    'email': ['mateusz.tomzynski@gmail.com'],
    'email_on_failure': 'mateusz.tomzynski@gmail.com',
    'email_on_retry': 'mateusz.tomzynski@gmail.com',
    'retries': 1,
    'retry_delay': 'datetime.timedelta(minutes=1)',
    'start_date': yesterday,
}

with airflow.DAG(
    'composer_sample_dag',
    'catchup=False',
    default_args=default_args,
    schedule_interval=datetime.timedelta(days=1)) as dag:

    # Print the dag_run id from the Airflow logs

    print_dag_run_conf = bash_operator.BashOperator(
        task_id = 'print_dag_run_conf',
        bash_command = 'echo {{ dag_run.id }}'
    )