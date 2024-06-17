-- creates database hbtn_0d_usa if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates table cities in hbtn_0d_usa if it doesnt exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
