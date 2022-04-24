from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime
import sqlite3
import pandas as pd
import os

from google.cloud import storage

path_airflow_study = '/home/tatiane/dataengineer/airflow-study/'

#salvar na GCP
def _salva_GCP(ti): 
    credentials_path = '/home/tatiane/airflow/dags/ivory-being-348021-7400d9333b88.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    filename = ti.xcom_pull(task_ids = 'consulta_sqlite')
    source_file_name = path_airflow_study + filename
    
    storage_client = storage.Client(credentials_path)
    bucket = storage_client.get_bucket('primeiro-bucket-tati')
    blob = bucket.blob(filename)
    blob.upload_from_filename(source_file_name)

#consulta db sqlite
def _consulta_sqlite():
    database_name = 'airflow-study.db'
    conn = sqlite3.connect(path_airflow_study + database_name)
    
    tabelas = pd.read_sql_query('SELECT NAME AS name FROM sqlite_master WHERE type = "table"', conn)
    
    #query
    param = tabelas['name'][0] #tabela contacts
    query = 'SELECT * FROM {}'.format(param)

    tabela = pd.read_sql_query(query, conn)
    tabela_name = 'tabela_airflow-study.csv'
    tabela.to_csv(path_airflow_study + tabela_name)
    
    return tabela_name

with DAG(
        'airflow-study_DAG',
       
        start_date = datetime(2022, 4,22),
        schedule_interval = '@daily'
        ) as dag:

    consulta_sqlite = PythonOperator(
        task_id = 'consulta_sqlite',
        python_callable = _consulta_sqlite
    )

    salva_GCP = PythonOperator(
        task_id = 'salva_GCP',
        python_callable = _salva_GCP
    )

    consulta_sqlite >> salva_GCP