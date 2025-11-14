-- Problema: 3480 - Cadeiras adjacentes | Resposta: Accepted
-- Linguagem: PostgreSQL [+0s]          | Tempo: 0.003s

SELECT c1.queue, c1.id "left", c2.id "right"
FROM chairs c1
LEFT JOIN chairs c2 ON c2.id = c1.id+1 AND c2.queue = c1.queue
WHERE (c1.available AND c2.available) IS TRUE
