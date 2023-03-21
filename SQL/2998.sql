SELECT c.name, c.investment, o.month month_of_payback, (so.acumulado - c.investment) return
FROM clients c
JOIN operations o ON (o.client_id = c.id)
JOIN 
    (SELECT o.client_id, o.month, 
        (SELECT SUM(op.profit) 
        FROM operations op 
        WHERE op.month <= o.month AND op.client_id = o.client_id) AS "acumulado"
    FROM operations o) so ON (so.client_id = c.id AND so.month = o.month)
WHERE (so.acumulado - c.investment) > 0
-- GROUP BY so.id, c.name, c.investment, o.month, so.acumulado
-- HAVING (so.acumulado - c.investment) > 0


SELECT *, 
    (SELECT SUM(op.profit) 
    FROM operations op 
    WHERE op.month <= o.month 
        AND op.client_id = o.client_id 
    HAVING (SUM(op.profit) - c.investment) > 0
    LIMIT 1) AS "acumulado"
FROM clients c 
JOIN operations o ON (o.client_id = c.id)