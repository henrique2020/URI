SELECT dep.nome AS "Departamento", e.nome AS "Empregado", s.valor AS "Salario Bruto", d.valor AS "Total Desconto", (s.valor-d.valor) AS "Salario Liquidoaws"
FROM departamento dep
JOIN divisao di ON (di.cod_dep = dep.cod_dep)
JOIN empregado e ON (e.lotacao = dep.cod_dep AND e.lotacao_div = di.cod_divisao)
LEFT JOIN -- SALÁRIO BRUTO
    (SELECT e.nome, SUM(COALESCE(v.valor, 0)) AS "valor"
    FROM empregado e
    LEFT JOIN emp_venc ev ON (ev.matr = e.matr)
    LEFT JOIN vencimento v ON (v.cod_venc = ev.cod_venc)
    GROUP BY e.nome) s ON (s.nome = e.nome)
LEFT JOIN -- DESCONTO
    (SELECT e.nome, SUM(COALESCE(d.valor, 0)) AS "valor"
    FROM empregado e
    LEFT JOIN emp_desc ed ON (ed.matr = e.matr)
    LEFT JOIN desconto d ON (d.cod_desc = ed.cod_desc)
    GROUP BY e.nome) d ON (d.nome = e.nome)
ORDER BY "Salario Liquidoaws" DESC