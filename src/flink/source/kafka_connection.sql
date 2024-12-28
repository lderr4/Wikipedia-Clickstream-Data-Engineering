CREATE TABLE kafka_clickstream_source (
    `id` STRING, 
    `user_id` STRING,
    `prev` STRING,
    `curr` STRING,
    `type` STRING,
    `click_time` TIMESTAMP(3),
    `processing_time` AS PROCTIME()
) WITH (
    'connector' = '{{ connector }}',
    'topic' = '{{ topic }}',
    'properties.bootstrap.servers' = '{{ bootstrap_servers }}',
    'properties.group.id' = '{{ consumer_group_id }}',
    'scan.startup.mode' = '{{ scan_stratup_mode }}',
    'format' = '{{ format }}'
);