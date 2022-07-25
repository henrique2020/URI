SELECT c.name, r.rentals_date
FROM rentals r 
JOIN customers c ON (c.id = r.id_customers)
WHERE to_char(r.rentals_date, 'YYYY-mm') = '2016-09'
