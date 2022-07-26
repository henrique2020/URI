SELECT name, CAST(salary/10 AS DECIMAL(10, 2)) AS tax
FROM people
WHERE salary > 3000
