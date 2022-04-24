#!/usr/bin/env python
# coding: utf-8

from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, unix_timestamp
from pyspark.sql import Row

from datetime import datetime, date
import string
import random
import time
import pandas as pd

spark = SparkSession.builder.getOrCreate()

row = []
for i in range(0, 500):
    row.append(('Fulano ' + str(i), random.randint(100,500), random.choice(['Cliente','Fornecedor'])))
    
df_spark = spark.createDataFrame(row, schema = 'nome string, valor long, tipo string')

timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

df_spark = df_spark.withColumn('datetime', unix_timestamp(lit(timestamp),'yyyy-MM-dd HH:mm:ss').cast("timestamp"))

