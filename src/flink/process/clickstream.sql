INSERT INTO postgres_clickstream_sink
SELECT         
    CAST(`id` AS STRING) AS click_id, 
    CAST(`user_id` AS STRING) AS user_id,
    CAST(`prev` AS STRING) AS previous_article,
    CAST(`curr` AS STRING) AS current_article,
    CAST(`type` AS STRING) AS click_type,
    CAST(`click_time` AS TIMESTAMP(3)) AS click_time
FROM kafka_clickstream_source;