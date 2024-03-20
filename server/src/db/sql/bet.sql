DROP TABLE IF EXISTS bet CASCADE;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT uuid_generate_v4();

CREATE TABLE bet (
    bet_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID,
    event_id UUID,
    team_id UUID,
    points INT
);