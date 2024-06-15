-- script list all records with a score 10 or higher
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
