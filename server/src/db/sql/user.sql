-- -- Drop table if it already exists

-- -- Create table
-- CREATE TABLE Users (
--     user_name varchar(100) PRIMARY KEY,
--     full_name varchar(500),
--     email varchar(100),
--     is_deleted BOOLEAN DEFAULT false,
--     session_id varchar(256));
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Drop table if it already exists
DROP TABLE IF EXISTS Users CASCADE;

SELECT uuid_generate_v4();

-- Create table
CREATE TABLE Users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_name varchar(100),
    full_name varchar(500),
    email varchar(100),
    password char(128),
    is_deleted BOOLEAN DEFAULT false,
    is_admin BOOLEAN DEFAULT false, -- key is referenced for user management from admin
    session_id char(256)
);
