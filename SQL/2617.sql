SELECT pd.name, pv.name
FROM products pd
JOIN providers pv ON (pv.id = pd.id_providers)
WHERE pv.name = 'Ajax SA'
