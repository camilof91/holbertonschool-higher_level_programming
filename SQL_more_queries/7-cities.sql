-- Create a database named 'hbtn_0d_usa' if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to the 'hbtn_0d_usa' database.
USE hbtn_0d_usa;
-- Create a table named 'cities' if it doesn't already exist.
-- The table has three columns: 'id' of type INT with AUTO_INCREMENT, UNIQUE, NOT NULL, and PRIMARY KEY constraints,
-- 'state_id' of type INT which must have a value for each row and is used as a foreign key referencing the 'id' column of the 'states' table,
-- and 'name' of type VARCHAR(256) which must have a value for each row.
CREATE TABLE IF NOT EXISTS cities(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);