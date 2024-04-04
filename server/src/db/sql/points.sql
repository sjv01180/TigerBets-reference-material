DROP TABLE IF EXISTS points CASCADE;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE points (
    points_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    points INT DEFAULT 0,
    CONSTRAINT fk_user
        FOREIGN KEY(user_id)
            REFERENCES Users(user_id)
            ON DELETE CASCADE
);
