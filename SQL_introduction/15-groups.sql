 -- selects the "score" column and counts the occurrences of each distinct score value in the
 -- "second_table" table. It uses the COUNT() function to count the occurrences and aliases
 -- the result as "number". The GROUP BY clause is used to group the results by the "score" 
 -- column, and the ORDER BY clause sorts the results in descending order based on the "score" column.
SELECT score, COUNT(*) AS number FROM hbtn_0c_0.second_table GROUP BY score ORDER BY number DESC;
