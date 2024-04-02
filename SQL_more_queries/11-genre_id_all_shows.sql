-- This query selects the 'title' column from the 'tv_shows' table,
-- and the 'genre_id' column from the 'tv_show_genres' table.
-- It renames the 'title' column as 'title' in the result set.
-- It retrieves all rows from the 'tv_shows' table, and the matching rows from the 'tv_show_genres' table.
-- It uses a LEFT JOIN to combine rows from both tables where the condition 'tv_shows.id = tv_show_genres.show_id' is met,
-- and includes all rows from the 'tv_shows' table even if there is no matching row in the 'tv_show_genres' table.
-- The results are ordered by 'title' in ascending order and 'genre_id' in ascending order.
SELECT tv_shows.title AS title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;