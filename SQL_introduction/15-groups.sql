 -- selects the "score" column and counts the occurrences of each distinct score value in the
SELECT score, COUNT(score) as number FROM second_table GROUP BY score ORDER BY number DESC;
