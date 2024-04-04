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

CREATE TABLE Users (
    user_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_name VARCHAR(100) UNIQUE NOT NULL,
    full_name VARCHAR(500),
    email VARCHAR(100) UNIQUE NOT NULL,
    is_deleted BOOLEAN DEFAULT false,
    session_id VARCHAR(256)
);