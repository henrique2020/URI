SELECT amount AS most_frequent_value
FROM (
  SELECT amount, COUNT(*)
  FROM value_table
  GROUP BY amount
  ORDER BY count DESC
  LIMIT 1
) AS qtde
