INSERT INTO postgres_clickstream_sink
SELECT         
    CAST(`id` AS INT) AS click_id, 
    CAST(`prev` AS STRING) AS previous_article,
    CAST(`curr` AS STRING) AS current_article,
    CAST(`type` AS STRING) AS click_type,
    CAST(`datetime_occured` AS TIMESTAMP(6)) AS click_time
FROM kafka_clickstream_source;