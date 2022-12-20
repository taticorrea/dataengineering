#!/bin/bash
date >> /Users/tcsilva/workspace/pessoal/estudos/dbt/jaffle_shop/test.txt
dbt run --model models/marts/core/fct_orders.sql  >> /Users/tcsilva/workspace/pessoal/estudos/dbt/jaffle_shop/test.txt
# dbt run --model /Users/tcsilva/workspace/pessoal/estudos/dbt/jaffle_shop/models/marts/core/fct_orders.sql
date >> /Users/tcsilva/workspace/pessoal/estudos/dbt/jaffle_shop/test.txt
