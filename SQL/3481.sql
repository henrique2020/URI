SELECT 
	DISTINCT
	n.node_id,
	CASE 
		WHEN n.pointer IS NULL THEN 'LEAF'
        WHEN p.node_id IS NULL THEN 'ROOT'
        ELSE 'INNER'
    END AS type
FROM nodes n
LEFT JOIN nodes p ON p.pointer = n.node_id
ORDER BY n.node_id
