#classe DAG
from airflow import DAG

#operadores
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator

#utils
from datetime import datetime
import pandas as pd
import requests
import json


#funcao que captura os dados
def captura_conta_dados():
    url = 'https://data.cityofnewyork.us/resource/rc75-m7u3.json'
    response = requests.get(url)
    df = pd.DataFrame(json.loads(response.content))
    qtd = len(df.index)
    return qtd

#funcao que verifica se os dados sao validos
def e_valido(ti):
    qtd = ti.xcom_pull(task_ids = 'captura_conta_dados')
    if (qtd > 10):
        return 'valido'
    return 'nao_valido'

with DAG(dag_id = 'count', 
         start_date = datetime(2022,4,19),
         schedule_interval = '30 * * * *',
         catchup = False) as dag:

    #task1 (capturar dados)
    captura_conta_dados = PythonOperator(
        task_id = 'captura_conta_dados',
        python_callable = captura_conta_dados
    )

    #task2 (printa que e valido)
    valido = BashOperator(
        task_id = 'valido',
        bash_command = "echo 'Quantidade OK!'"

    )

    #task3 (printa que nao e valido)
    nao_valido = BashOperator(
        task_id = 'nao_valido',
        bash_command = "echo 'Quantidade não está OK!'"

    )

    #pega resultado da task1
    e_valido = BranchPythonOperator(
        task_id = 'e_valido',
        python_callable = e_valido
    )

    #ordem das tasks
    captura_conta_dados >> e_valido >> [valido, nao_valido]

