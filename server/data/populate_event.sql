\set teamA '4a0c8c25-e548-4110-a3a9-f44f6a4256a4'
\set teamB '5e1dbdd3-aa30-456b-9820-e3e7825b9bb9'
\set teamC '6d83e946-46c5-494e-a788-bf3e85a466a4'
\set teamD '61c70f68-a3a5-404e-9102-a9effbb5b386'

-- Insert into team table
INSERT INTO team (team_id, team_name) VALUES 
(:teamA, 'Team A'),
(:teamB, 'Team B'),
(:teamC, 'Team C'),
(:teamD, 'Team D');

-- Insert into events table
INSERT INTO events (event_id, event_name, team_a_id, team_b_id) VALUES 
('8df7f992-d6b7-4654-9e3f-9dedbf4c54bf', 'RIT Random Event', :teamA, :teamB),
('a7a3afc2-3f4a-4aeb-8c06-9e667c5b4f67', 'Second', :teamC, :teamD),
('c7fd33bc-f8c4-4b5e-b1aa-9f2e4c4a6b88', 'Third', :teamA, :teamB);
