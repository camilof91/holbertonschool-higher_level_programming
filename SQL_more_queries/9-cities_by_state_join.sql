-- Selects the 'id' and 'name' columns from the 'cities' table,
-- and also selects the 'name' column from the 'states' table.
-- It retrieves rows where there is a match between the 'state_id' column in the 'cities' table
-- and the 'id' column in the 'states' table.
-- It uses an INNER JOIN to combine rows from both tables where the condition 'cities.state_id = states.id' is met.
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;