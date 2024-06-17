-- creates database hbtn_0d_2 if it doesnt exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
USE hbtn_0d_2;

-- create the user user_0d_2 if they don't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to the user on the current database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Flush privileges to ensure the changes take effect immediately
FLUSH PRIVILEGES;
