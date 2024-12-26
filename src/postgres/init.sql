CREATE SCHEMA clickstream;

SET
    search_path TO clickstream;

CREATE TABLE clicks (
    click_id int PRIMARY KEY,
    previous_article VARCHAR,
    current_article VARCHAR,
    click_type VARCHAR,
    click_time TIMESTAMP
)