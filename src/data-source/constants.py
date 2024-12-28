clickstream_data_path = "app/data/clickstream-nlwiki-2024-10.tsv"
clickstream_data_headers = ['prev', 'curr', 'type', 'n']

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



