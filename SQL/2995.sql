SELECT temperature, COUNT(mark)
FROM records
GROUP BY temperature, mark
ORDER BY mark
