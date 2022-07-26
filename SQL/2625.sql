SELECT REGEXP_REPLACE(cpf, '(\d{3})(\d{3})(\d{3})', '\1.\2.\3-') AS CPF FROM natural_person
