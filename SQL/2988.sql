SELECT t.name, 
	(mt1.matches + mt2.matches) AS matches, 
    (mt1.victories + mt2.victories) AS victories, 
    (mt1.defeats + mt2.defeats) AS defeats, 
    (mt1.draws + mt2.draws) AS draws,
    ((mt1.victories + mt2.victories)*3 + (mt1.draws + mt2.draws)) AS score
FROM teams t
JOIN (
  SELECT team_1 AS id, COUNT(1) AS matches,
      SUM(CASE WHEN team_1_goals > team_2_goals THEN 1 ELSE 0 END) AS victories,
      SUM(CASE WHEN team_1_goals < team_2_goals THEN 1 ELSE 0 END) AS defeats,
      SUM(CASE WHEN team_1_goals = team_2_goals THEN 1 ELSE 0 END) AS draws
  FROM matches
  GROUP BY team_1
) mt1 ON mt1.id = t.id
JOIN (
  SELECT team_2 AS id, COUNT(1) AS matches,
      SUM(CASE WHEN team_1_goals < team_2_goals THEN 1 ELSE 0 END) AS victories,
      SUM(CASE WHEN team_1_goals > team_2_goals THEN 1 ELSE 0 END) AS defeats,
      SUM(CASE WHEN team_1_goals = team_2_goals THEN 1 ELSE 0 END) AS draws
  FROM matches
  GROUP BY team_2
) mt2 ON mt2.id = t.id
ORDER BY score DESC
