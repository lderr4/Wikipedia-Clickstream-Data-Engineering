CREATE SCHEMA clickstream;

SET
    search_path TO clickstream;


DROP TABLE IF EXISTS clicks;
CREATE TABLE clicks (
    click_id VARCHAR PRIMARY KEY,
    user_id VARCHAR,
    previous_article VARCHAR,
    current_article VARCHAR,
    click_type VARCHAR,
    click_time TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS users CASCADE;
CREATE TABLE users (
    id VARCHAR PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    street_address VARCHAR,
    city VARCHAR,
    state VARCHAR,
    country VARCHAR,
    postal_code VARCHAR,
    email VARCHAR,
    username VARCHAR,
    date_of_birth TIMESTAMPTZ,
    registered_date TIMESTAMPTZ,
    phone VARCHAR,
    picture VARCHAR
);