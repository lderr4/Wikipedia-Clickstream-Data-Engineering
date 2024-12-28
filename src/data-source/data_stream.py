from pandas import read_csv
from constants import clickstream_data_path, clickstream_data_headers, kafka_topic_name, kafka_broker_url
from users_init import users_init
from numpy import array
from numpy.random import choice
from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import logging
import time
from json import dumps
from uuid import uuid4
from datetime import datetime
logging.getLogger().setLevel(logging.INFO)

def create_topic_in_kafka():
    try:
        admin_client = KafkaAdminClient(
        bootstrap_servers=[kafka_broker_url], 
        client_id='create_topic'
        )

        all_topics = admin_client.list_topics()
        if kafka_topic_name in all_topics:
            logging.info(f"Topic {kafka_topic_name} already exists. Proceeding to next step.")
            return
        
        admin_client.create_topics(new_topics=[NewTopic(name=kafka_topic_name, num_partitions=1, replication_factor=1)], validate_only=False)
        logging.info(f"Topic <{kafka_topic_name}> created successfully.")

    except Exception as e:
        logging.error(f"Failed to create topic due to: {e}")




def setup_data_source():
    try:
        df = read_csv(clickstream_data_path, 
                        sep='\t',
                        on_bad_lines='skip',
                        header=None,
                        names=clickstream_data_headers)
        
        total_clicks = df['n'].sum()

        click_probabilities = array(df["n"] / total_clicks)
        logging.info(f'Clickstream data source created succesfully.')
        return df, click_probabilities 
    
    except Exception as e:
        logging.error(f'Error setting up clickstream data source: {e}')



def stream_data(df, click_probabilities, ids, seconds=10):
    

    producer = KafkaProducer(bootstrap_servers=[kafka_broker_url], max_block_ms=5000)
    start = time.time()
    i = 0
    while True:
        time.sleep(1)
        # if start + seconds < time.time():
        #     break
        try:
            choice_idx = choice(df.index, p=click_probabilities)
            click_dict = df.iloc[choice_idx].to_dict()
            del click_dict['n']
            
            click_dict['id'] = uuid4()

            user_id = choice(ids)
            click_dict["user_id"] = user_id
            datetime_occured = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            click_dict['click_time'] = datetime_occured
            
            
            producer.send(kafka_topic_name, dumps(click_dict, default=str).encode('utf-8'))

            i += 1 
            
            logging.info(f'Data sent to topic <{kafka_topic_name}> for Wikipedia Article Name: <{ click_dict["curr"] }>. Timestamp: {datetime_occured}')
        
        except Exception as e:
            logging.error(f'An error occured: {e}')





if __name__ == "__main__":
    ids = users_init()
    df, click_probabilities = setup_data_source()
    create_topic_in_kafka()
    stream_data(df, click_probabilities, ids)
