SELECT city_name, population
FROM cities
WHERE population IN (
    (
      SELECT MAX(population)
      FROM cities
      WHERE population < (
          SELECT MAX(population)
          FROM cities
        )
    ),
  	(
      SELECT MIN(population)
    	FROM cities
    	WHERE population > (
        	SELECT MIN(population)
        	FROM cities
    	)
    )
 )
 ORDER BY population DESC
