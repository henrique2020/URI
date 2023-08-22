SELECT name
FROM
(
    SELECT CONCAT('Podium:', team) AS name, position FROM league LIMIT 3
    UNION 
    SELECT CONCAT('Demoted:', team) AS name, position FROM league ORDER BY position DESC LIMIT 2
) AS league
ORDER BY position
