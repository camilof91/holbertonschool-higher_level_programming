-- Create a table named 'id_not_null' if it doesn't already exist.
-- The table has two columns: 'id' of type INT with a default value of 1,
-- and 'name' of type VARCHAR(256) which allows NULL values.
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);