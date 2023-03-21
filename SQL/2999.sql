SELECT e.nome nome, SUM(s.valor-d.valor) salario
FROM departamento dep
JOIN divisao di ON (di.cod_dep = dep.cod_dep)
JOIN empregado e ON (e.lotacao = dep.cod_dep AND e.lotacao_div = di.cod_divisao)
LEFT JOIN -- SALÁRIO
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
LEFT JOIN -- MEDIA DA DIVISÃO
    (SELECT di.cod_divisao divisao, ROUND(AVG(s.valor-d.valor), 2) AS media
    FROM departamento dep
    JOIN divisao di ON (di.cod_dep = dep.cod_dep)
    JOIN empregado e ON (e.lotacao = dep.cod_dep AND e.lotacao_div = di.cod_divisao)
    LEFT JOIN 
        (SELECT e.nome, SUM(COALESCE(v.valor, 0)) AS "valor"
        FROM empregado e
        LEFT JOIN emp_venc ev ON (ev.matr = e.matr)
        LEFT JOIN vencimento v ON (v.cod_venc = ev.cod_venc)
        GROUP BY e.nome) s ON (s.nome = e.nome)
    LEFT JOIN 
        (SELECT e.nome, SUM(COALESCE(d.valor, 0)) AS "valor"
        FROM empregado e
        LEFT JOIN emp_desc ed ON (ed.matr = e.matr)
        LEFT JOIN desconto d ON (d.cod_desc = ed.cod_desc)
        GROUP BY e.nome) d ON (d.nome = e.nome)
    GROUP BY di.cod_divisao) med ON (med.divisao = di.cod_divisao)
WHERE (s.valor-d.valor) > med.media AND (s.valor-d.valor) > 8000
GROUP BY e.lotacao_div, e.nome
ORDER BY e.lotacao_div;