import pendulum
from airflow import DAG
from airflow.operators.python import PythonOperator
import sys

sys.path.append("/opt/airflow")

from pipeline.pipeline_projeto import  extract, transform, load

def run_pipeline():
    df = extract()
    df_titulo, df_movimentacao = transform(df)
    load(df_titulo, df_movimentacao)

with DAG (
    dag_id = "Vendas_ELT",
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

    