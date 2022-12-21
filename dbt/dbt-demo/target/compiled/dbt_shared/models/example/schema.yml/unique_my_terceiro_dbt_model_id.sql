
    
    

select
    id as unique_field,
    count(*) as n_records

from schema_dbt.my_terceiro_dbt_model
where id is not null
group by id
having count(*) > 1


