-- Create a table named 'force_name' if it doesn't already exist.
-- The table has two columns: 'id' of type INT and 'name' of type VARCHAR(255).
-- The 'name' column is defined as NOT NULL, meaning it must have a value for each row.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(255) NOT NULL
);