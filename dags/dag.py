import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys

sys.path.append("/opt/airflow")

from pipeline.pipeline_projeto import  extract, transform, load

default_args= {
    "owner" : "airflow",
    "depends_on_past" : False,
    "email_on_failure" : False,
    "email_on_retry" : False,
    "retries" : 1,
    "retry_delay" : pendulum.duration(minutes = 5) 
}

def run_pipeline():
    df = extract()
    df_titulo, df_movimentacao = transform(df)
    load(df_titulo, df_movimentacao)

with DAG (
    dag_id = "Vendas_ELT",
    default_args = default_args,
    description = "Projeto Engenharia de Dados + DevOps",
    start_date = pendulum.datetime(2026, 1, 25, tz= "America/Sao_Paulo"),
    catchup = False,
    schedule = None,
    tags = ['Projeto', 'DataOps']
) as dag:
    
    pipeline = PythonOperator(
        task_id = "Pipeline",
        python_callable = run_pipeline
    )

    