-- This query selects the 'title' column from the 'tv_shows' table and renames it as 'title' in the result set.
-- It retrieves rows from the 'tv_shows' table, the 'tv_show_genres' table, and the 'tv_genres' table,
-- where there are matches between the 'id' column in the 'tv_shows' table and the 'show_id' column in the 'tv_show_genres' table,
-- between the 'id' column in the 'tv_genres' table and the 'genre_id' column in the 'tv_show_genres' table,
-- and where the value in the 'name' column of the 'tv_genres' table is equal to "Comedy".
-- It uses INNER JOINs to combine rows from these tables based on the specified conditions.
-- The results are ordered by 'title' in ascending order.
SELECT tv_shows.title AS title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy"
ORDER BY title;