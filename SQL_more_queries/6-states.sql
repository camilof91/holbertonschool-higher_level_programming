-- Create a database named 'hbtn_0d_usa' if it doesn't already exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Switch to the 'hbtn_0d_usa' database.
USE hbtn_0d_usa;
-- Create a table named 'states' if it doesn't already exist.
-- The table has two columns: 'id' of type INT with AUTO_INCREMENT, UNIQUE, NOT NULL, and PRIMARY KEY constraints,
-- and 'name' of type VARCHAR(256) which must have a value for each row.
CREATE TABLE IF NOT EXISTS states(
    id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);