SELECT p.name pName, c.name cName
FROM products p
JOIN categories c ON (c.id = p.id_categories)
WHERE p.amount > 100 AND c.id IN (1, 2, 3, 6, 9)
ORDER BY c.id
