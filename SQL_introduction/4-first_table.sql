--  creates a table named "first_table" with two columns: "id" of type INT and "name" 
-- of type VARCHAR with a maximum length of 256 characters.
--  characters only if it does not exist.
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
