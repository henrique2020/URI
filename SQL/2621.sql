SELECT pd.name
FROM products pd
JOIN providers pv ON (pv.id = pd.id_providers)
WHERE (pd.amount >= 10 AND pd.amount <= 20) AND pv.name LIKE ('P%')
