(SELECT CONCAT('Podium: ', team) AS name FROM league ORDER BY position ASC LIMIT 3)
UNION
(SELECT CONCAT('Demoted: ', team) AS name FROM league ORDER BY position DESC LIMIT 2)
