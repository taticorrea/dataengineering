from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator

from datetime import datetime
import sqlite3
import pandas as pd
import random
import os

#from google.cloud import storage

path_airflow_study = '/home/tatiane/dataengineering-study/airflow-study/dataingestion'
database_name = 'airflow-study.db'
tabela_name = 'tabela.csv'

#credenciais gcs
credentials_path = path_airflow_study + 'ivory-being-348021-7400d9333b88.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path



'''
#salvar na GCS
def _salva_GCS(ti): 
    credentials_path = '/home/tatiane/airflow/dags/ivory-being-348021-7400d9333b88.json'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

    filename = ti.xcom_pull(task_ids = 'consulta_sqlite')
    source_file_name = path_airflow_study + filename
    
    storage_client = storage.Client(credentials_path)
    bucket = storage_client.get_bucket('primeiro-bucket-tati')
    blob = bucket.blob(filename)
    blob.upload_from_filename(source_file_name)
'''

#cria db sqlite
def _cria_consulta_sqlite():
    #criando db
    conn = sqlite3.connect(path_airflow_study + database_name)
    
    #instanciando cursor
    cur = conn.cursor()
    
    #criando tabela
    sql_create = 'CREATE TABLE IF NOT EXISTS teste '\
    '(id integer primary key, '\
    'valor integer, '\
    'categoria varchar(140))'
    cur.execute(sql_create)

    #criando linhas para a tabela
    row = []
    for i in range(0, 500):
        row.append((str(i), random.randint(100,500), random.choice(['Cliente','Fornecedor'])))
    
    #inserindo registros
    sql_insert = 'INSERT OR IGNORE INTO teste values (?, ?, ?)'

    for rec in row:
        cur.execute(sql_insert, rec)

    conn.commit()
    
    #pegando tabela teste
    tabelas = pd.read_sql_query('SELECT NAME AS name FROM sqlite_master WHERE type = "table"', conn)
    param = tabelas['name'][0]
    
    #query
    query = 'SELECT * FROM {}'.format(param)

    tabela = pd.read_sql_query(query, conn)
    tabela.to_csv(path_airflow_study + tabela_name)
    
    return tabela_name


with DAG(
        'airflow-study_DAG',       
        start_date = datetime(2022, 4,22),
        schedule_interval = '@daily'
        ) as dag:

    cria_consulta_sqlite = PythonOperator(
        task_id = 'consulta_sqlite',
        python_callable = _cria_consulta_sqlite
    )
    
    upload_gcs = LocalFilesystemToGCSOperator(
        task_id = 'upload_gcs',
        src = path_airflow_study + tabela_name,
        dst = tabela_name,
        bucket = 'primeiro-bucket-tati'

    )
    '''
    salva_GCP = PythonOperator(
        task_id = 'salva_GCP',
        python_callable = _salva_GCP
    )
    '''
cria_consulta_sqlite >> upload_gcs  