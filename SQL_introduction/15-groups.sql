-- This query retrieves the score of each record in the "second_table" table
-- and counts how many times each score appears in the table.
-- Then, it groups the results by score using the GROUP BY clause.
-- After that, it sorts the results in descending order based on the number of records
-- with the same score using the ORDER BY clause.
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY number DESC;
