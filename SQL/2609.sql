SELECT c.name, SUM(p.amount) 
FROM products p 
JOIN categories c ON (c.id = p.id_categories)
GROUP BY c.name
