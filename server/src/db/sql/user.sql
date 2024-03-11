-- Drop table if it already exists
DROP TABLE IF EXISTS Users CASCADE;


-- Create table
CREATE TABLE Users (
    user_name varchar(100) PRIMARY KEY,
    full_name varchar(500),
    email varchar(100),
    is_deleted BOOLEAN DEFAULT false
);
