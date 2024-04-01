-- selects the "score" and "name" columns from the "second_table" table where the value in 
-- the "score" column is greater than or equal to 10. It then orders the results in descending 
-- order based on the "score" column.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
