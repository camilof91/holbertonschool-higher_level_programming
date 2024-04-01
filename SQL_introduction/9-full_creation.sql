-- creates a table named "second_table" with three columns: "id" of type INT, "name" of type VARCHAR with
-- a maximum length of 256 characters, and "score" of type INT.
CREATE TABLE IF NOT EXISTS second_table(
    id INT,
    name VARCHAR(256),
    score INT
);

-- Inserts four records into the "second_table"
INSERT INTO second_table (id, name, score)
VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
