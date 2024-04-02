-- Create a table named 'unique_id' if it doesn't already exist.
-- The table has two columns: 'id' of type INT with a default value of 1,
-- and 'name' of type VARCHAR(256).
-- The 'id' column is defined as UNIQUE, ensuring that each value in the column is unique across all rows.
CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
