-- creates database hbtn_0d_usa if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates table states in hbtn_0d_usa if it doesnt exist
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
