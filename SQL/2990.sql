SELECT e.cpf, e.enome, d.dnome
FROM empregados e
JOIN departamentos d ON (d.dnumero = e.dnumero)
WHERE e.cpf NOT IN (SELECT cpf_emp FROM trabalha)
ORDER BY e.cpf
