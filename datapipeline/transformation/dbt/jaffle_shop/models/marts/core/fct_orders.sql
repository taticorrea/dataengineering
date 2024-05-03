with orders as (

    select * from {{ ref('stg_orders') }}

),
payments as (

    select * from {{ ref('stg_payments') }}

),
orders_customer as (
    select 
        order_id,
        customer_id
    from orders
),
orders_payments as (
    select 
        order_id,
        amount
    from payments
),
final as (
    select 
        orders_customer.order_id, 
        orders_customer.customer_id,
        orders_payments.amount,
        case 
            when orders_payments.amount > 2000
                then 'Valores altos'
            when orders_payments.amount > 3000
                then 'Valores muito altos'
            else 'Valores baixos'
        end as tipo
    from orders_payments
    left join orders_customer using (order_id)
)

select * from final