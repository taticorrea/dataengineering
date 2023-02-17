from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .getOrCreate()

#Databricks
def grants_by_group(databases: list, tables: list, group: str):

    df_databases = spark.createDataFrame([("","","","")]).toDF(*schema)
    df_tables = spark.createDataFrame([("","","","")]).toDF(*schema)
        
    if len(databases) == 0:
        databases = spark.sql('show databases')
        databases = [i.databaseName for i in databases.collect()]
        
    for databaseName in databases:
        #pegando grants de um determinado grupo em um determinado database
        grants_database = spark.sql(f'show grants `{group}` ON DATABASE {databaseName}')

        #fazendo union com dataframe de databases criado vazio antes do loop
        df_databases = df_databases.unionAll(grants_database)

#     if len(tables) == 0:
#         spark.sql(f'use {databaseName}')
#         table = spark.sql('show tables')
#         all_tables_list = [i.tableName for i in table.collect()]

#         tables = all_tables_list

#         for tableName in tables:
#             datasetName = databaseName + '.' + tableName
#             grants_table = spark.sql(f'show grants `{group}` ON TABLE {datasetName}')
#             df_tables = df_tables.unionAll(grants_table)
        
    return df_databases.display()

#lista de databases 
databases = []

#lista de tabelas 
tables = []

#grupo de acesso
group=''

grants_by_group(databases,tables,group)    