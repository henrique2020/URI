SELECT dep.nome AS "Nome Departamento", COUNT(e.nome) AS "Numero de Empregados", ROUND(AVG(s.valor-d.valor), 2) AS "Media Salarial", MAX(s.valor-d.valor) AS "Maior Salario", MIN(s.valor-d.valor) AS "Menor Salario"
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
GROUP BY dep.nome
ORDER BY AVG(s.valor-d.valor) DESC;