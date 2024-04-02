-- Create a database 'hbtn_0d_2' if it doesn't already exist.
-- Create a user 'user_0d_2' identified by the password 'user_0d_2_pwd' if the user doesn't already exist.
-- Grant SELECT privilege on all tables within the 'hbtn_0d_2' database to the user 'user_0d_2' when connecting from 'localhost'.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2; CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd'; GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
