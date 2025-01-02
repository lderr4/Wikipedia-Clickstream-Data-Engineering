clickstream_data_path = "data/clickstream-enwiki-2024-10.tsv"
clickstream_data_headers = ['prev', 'curr', 'type', 'n']
clickstream_sample_path = "app/src/data/clickstream-enwiki-2024-10_sample.csv"

kafka_topic_name = "clickstream"
kafka_broker_url = "broker:29092"

postgres_db_config = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "postgres",  # or the host of your PostgreSQL server
    "port": 5432  # default PostgreSQL port
}

random_user_endpoint = 'https://randomuser.me/api/?results=5000'



