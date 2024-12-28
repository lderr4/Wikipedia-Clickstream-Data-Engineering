CREATE TABLE postgres_clickstream_sink (
    click_id STRING,
    user_id STRING,
    previous_article VARCHAR,
    current_article VARCHAR,
    click_type VARCHAR,
    click_time TIMESTAMP(3)
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:postgresql://{{ host }}:{{ port }}/postgres',
    'table-name' = '{{ schema_name }}.{{ table_name }}',
    'username' = '{{ username }}',
    'password' = '{{ password }}',
    'driver' = 'org.postgresql.Driver'
)