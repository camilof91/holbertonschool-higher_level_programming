-- Selects the 'title' column from the 'tv_shows' table, 
-- and the 'genre_id' column from the 'tv_show_genres' table. 
-- It renames the 'title' column as 'title' in the result set.
-- It retrieves rows where there is a match between the 'id' column in the 'tv_shows' table
-- and the 'show_id' column in the 'tv_show_genres' table.
-- It uses an INNER JOIN to combine rows from both tables where the condition 'tv_shows.id = tv_show_genres.show_id' is met.
-- The results are ordered by 'title' in ascending order and 'genre_id' in ascending order.
SELECT tv_shows.title AS title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;