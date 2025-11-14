-- Problema: 3482 - Seguidores | Resposta: Accepted
-- Linguagem: PostgreSQL [+0s] | Tempo: 0.004s

SELECT u1.user_name u1_name, u2.user_name u2_name
FROM users u1
JOIN followers f1 ON f1.user_id_fk = u1.user_id
JOIN users u2 ON u2.user_id = f1.following_user_id_fk AND u2.posts > u1.posts
JOIN followers f2 ON f2.user_id_fk = u2.user_id AND f2.following_user_id_fk = u1.user_id
ORDER BY u1.user_id
