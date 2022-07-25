SELECT pd.name, pv.name, pd.price
FROM products pd
JOIN providers pv ON (pv.id = pd.id_providers)
JOIN categories c ON (c.id = pd.id_categories)
WHERE pd.price > 1000 AND c.name = 'Super Luxury'
