-- lists the number of records with matching scores in second_table
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score
ORDER BY score DESC;
