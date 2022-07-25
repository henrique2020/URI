SELECT id, name
FROM customers
WHERE id NOT IN(SELECT DISTINCT id_customers FROM locations)
ORDER BY id
