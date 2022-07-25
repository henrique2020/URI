SELECT c.name 
FROM legal_person l
JOIN customers c ON (c.id = l.id_customers)
