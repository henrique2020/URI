SELECT lf.name, ROUND((lf.omega*1.618), 3) AS "Fator N"
FROM dimensions d
JOIN life_registry lf ON (lf.dimensions_id = d.id)
WHERE d.name IN ('C875', 'C774') AND lf.name LIKE 'Richard%'
ORDER BY lf.omega
