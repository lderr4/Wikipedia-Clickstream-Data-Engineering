CREATE TABLE postgres_clickstream_sink (
    click_id int,
    previous_article VARCHAR,
    current_article VARCHAR,
    click_type VARCHAR,
    click_time TIMESTAMP
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:postgresql://{{ host }}:{{ port }}/postgres',
    'table-name' = '{{ schema_name }}.{{ table_name }}',
    'username' = '{{ username }}',
    'password' = '{{ password }}',
    'driver' = 'org.postgresql.Driver'
)