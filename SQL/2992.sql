SELECT c.departamento, c.divisao, c.media
FROM departamento dep
JOIN 
	(SELECT dep.nome AS "departamento", di.nome AS "divisao", ROUND(SUM(s.valor - d.valor)/COUNT(e.nome), 2) AS "media", ROW_NUMBER() OVER(PARTITION BY dep.nome ORDER BY SUM(s.valor - d.valor)/COUNT(e.nome) DESC) linha
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
    GROUP BY dep.nome, di.nome) c ON (c.departamento = dep.nome AND c.linha = 1)
ORDER BY c.media DESC;