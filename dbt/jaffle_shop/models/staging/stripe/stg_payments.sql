select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    amount,
    status

from {{   source('stripe','stripe_payments')  }}