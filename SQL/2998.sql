SELECT c.name, c.investment, MIN(o.month) as month_of_payback, MIN(o.profit) - c.investment as return
FROM clients c
JOIN (
    SELECT o.client_id, o.month, SUM(op.profit) profit
    FROM operations o
    JOIN operations op ON (op.client_id = o.client_id AND op.month <= o.month)
    GROUP BY o.client_id, o.month
) o ON o.client_id = c.id AND o.profit >= c.investment
GROUP BY c.name, c.investment
ORDER BY return DESC
