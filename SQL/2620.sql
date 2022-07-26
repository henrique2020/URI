SELECT c.name, o.id
FROM orders o
JOIN customers c ON (c.id = o.id_customers)
WHERE o.orders_date BETWEEN '2016-01-01' AND '2016-06-30'
