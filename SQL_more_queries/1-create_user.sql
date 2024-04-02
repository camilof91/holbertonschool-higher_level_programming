-- Create a user 'user_0d_1' identified by the password 'user_0d_1_pwd' if the user doesn't already exist.
-- Grant all privileges on all databases and tables to the user 'user_0d_1' when connecting from 'localhost'.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';