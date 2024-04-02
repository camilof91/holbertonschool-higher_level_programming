-- This query selects the 'title' column from the 'tv_shows' table and renames it as 'title' in the result set,
-- and selects the 'name' column from the 'tv_genres' table and renames it as 'name' in the result set.
-- It retrieves all rows from the 'tv_shows' table, and the matching rows from the 'tv_show_genres' table and the 'tv_genres' table,
-- using LEFT JOINs to combine rows from these tables based on the conditions 'tv_shows.id = tv_show_genres.show_id' 
-- and 'tv_genres.id = tv_show_genres.genre_id'.
-- The LEFT JOIN ensures that all rows from the 'tv_shows' table are included in the result set, 
-- even if there are no matching rows in the 'tv_show_genres' or 'tv_genres' tables.
-- The results are ordered by 'title' in ascending order, and then by 'name' in ascending order.
SELECT tv_shows.title AS title,
       tv_genres.name AS name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, name;