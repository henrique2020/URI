SELECT * 
FROM (
    SELECT name, customers_number FROM lawyers WHERE customers_number = (SELECT MAX(customers_number) FROM lawyers)
    UNION
    SELECT name, customers_number FROM lawyers WHERE customers_number = (SELECT MIN(customers_number) FROM lawyers)
    UNION
    SELECT 'Average', CAST(AVG(customers_number) AS INTEGER) FROM lawyers
) AS lawyers
ORDER BY name = 'Average', customers_number DESC
