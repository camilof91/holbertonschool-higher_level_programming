-- This query selects the 'title' column from the 'tv_shows' table,
-- and the 'genre_id' column from the 'tv_show_genres' table.
-- It renames the 'title' column as 'title' in the result set.
-- It retrieves rows from the 'tv_shows' table and the matching rows from the 'tv_show_genres' table,
-- where there is no matching row in the 'tv_show_genres' table (i.e., the 'genre_id' is NULL).
-- It uses a LEFT JOIN to combine rows from both tables based on the condition 'tv_shows.id = tv_show_genres.show_id',
-- and filters the result set to include only those rows where 'genre_id' is NULL.
-- The results are ordered by 'title' in ascending order and 'genre_id' in ascending order.
SELECT tv_shows.title AS title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;