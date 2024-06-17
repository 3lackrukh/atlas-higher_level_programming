-- creates the table unique_id if it doesnt exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256)
);
