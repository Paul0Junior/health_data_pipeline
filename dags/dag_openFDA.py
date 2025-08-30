from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
import pendulum

with DAG(
    dag_id='dag_OpenFDA',
    schedule=None,
    start_date=pendulum.datetime(2025, 1, 1, tz='GMT'),
    catchup=False,
    tags=['openfda']
) as dag:

    extract_task = BashOperator(
        task_id='extract_task',
        bash_command='python3 /opt/airflow/dags/scripts/OpenFDA/extract.py',
    )

    extract_task