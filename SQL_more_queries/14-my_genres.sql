-- This query selects the 'name' column from the 'tv_genres' table and renames it as 'name' in the result set.
-- It retrieves rows from the 'tv_genres' table, the 'tv_show_genres' table, and the 'tv_shows' table,
-- where there are matches between the 'id' column in the 'tv_genres' table and the 'genre_id' column in the 'tv_show_genres' table,
-- and between the 'id' column in the 'tv_shows' table and the 'show_id' column in the 'tv_show_genres' table.
-- It uses INNER JOINs to combine rows from these tables based on the specified conditions.
-- It filters the result set to include only those rows where the 'title' column in the 'tv_shows' table is equal to "Dexter".
-- The results are ordered by 'name' in ascending order.
SELECT tv_genres.name AS name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter"
ORDER BY name;
