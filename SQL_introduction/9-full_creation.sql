-- Attempt to create second_table in the specified database
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- create records for John, Alex, Bob, George
INSERT INTO  second_table (id, name, score)
VALUES 
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
