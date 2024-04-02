-- This query selects the 'name' column from the 'tv_genres' table and renames it as 'genre' in the result set.
-- It also counts the number of occurrences of 'genre_id' from the 'tv_show_genres' table and renames it as 'number_of_shows' in the result set.
-- It retrieves rows from the 'tv_genres' table and the matching rows from the 'tv_show_genres' table,
-- where there is a match between the 'id' column in the 'tv_genres' table and the 'genre_id' column in the 'tv_show_genres' table.
-- It uses a LEFT JOIN to combine rows from both tables based on the condition 'tv_genres.id = tv_show_genres.genre_id'.
-- It filters the result set to include only those rows where 'genre_id' is not NULL.
-- It groups the result set by 'name' column from the 'tv_genres' table.
-- The results are ordered by 'number_of_shows' in descending order.
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
