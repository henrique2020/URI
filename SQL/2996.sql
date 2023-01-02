SELECT p.year, us.name AS sender, ur.name AS receiver
FROM packages P
JOIN users us ON (us.id = p.id_user_sender AND us.address <> 'Taiwan')
JOIN users ur ON (ur.id = p.id_user_receiver AND ur.address <> 'Taiwan')
WHERE p.color = 'blue' OR p.year = 2015
ORDER BY p.year DESC
