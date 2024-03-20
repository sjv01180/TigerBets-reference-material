DROP TABLE IF EXISTS events CASCADE;
DROP TABLE IF EXISTS team CASCADE;

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE team (
    team_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    team_name VARCHAR(255) NOT NULL
);

CREATE TABLE events (
    event_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_name VARCHAR(255) NOT NULL,
    team_a_id UUID,
    team_b_id UUID,
    event_result VARCHAR(255),
    FOREIGN KEY (team_a_id) REFERENCES team (team_id) ON DELETE SET NULL,
    FOREIGN KEY (team_b_id) REFERENCES team (team_id) ON DELETE SET NULL
);

