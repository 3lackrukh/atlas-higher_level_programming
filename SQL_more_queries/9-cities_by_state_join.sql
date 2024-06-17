-- lists all cities contained in database hbtn_0d_usa
SELECT c.id, c.name, s.name AS state_name
FROM cities c
INNER JOIN states s ON c.state_id = s.id
ORDER BY  c.id ASC;
