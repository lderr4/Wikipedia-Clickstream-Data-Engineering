from psycopg2 import connect
from psycopg2.extras import execute_values
from requests import get
from uuid import uuid4
from constants import postgres_db_config, random_user_endpoint
import logging

"https://github.com/"

def get_raw_data(url):
    response = get(url).json()
    response = response['results']
    return response


def transform_raw_data(raw_data):
    dataset = []
    for res in raw_data:
        data = {}
        location = res['location']
        
        data['id'] = uuid4()
        data['first_name'] = res['name']['first']
        data['last_name'] = res['name']['last']
        data['gender'] = res['gender']
        data['street_address'] = f"{str(location['street']['number'])} {location['street']['name']}"
        data['city'] = location['city']
        data['state'] = location['state']
        data['country'] = location['country']
        data['postal_code'] = location['postcode']
        data['email'] = res['email']
        data['username'] = res['login']['username']
        data['dob'] = res['dob']['date']
        data['registered_date'] = res['registered']['date']
        data['phone'] = res['phone']
        data['picture'] = res['picture']['medium']
        
        dataset.append(data)
        
    ids = [str(data["id"]) for data in dataset]
        
    dataset = [
            (
                str(user['id']),
                user['first_name'],
                user['last_name'],
                user['gender'],
                user['street_address'],
                user['city'],
                user['state'],
                user['country'],
                str(user['postal_code']),
                user['email'],
                user['username'],
                user['dob'],
                user['registered_date'],
                user['phone'],
                user['picture']
            )
            for user in dataset
        ]
    
    return ids, dataset


def db_connect(config):
    connection = None
    try:
        connection = connect(**config)
    except Exception as e:
        logging.error(f"Failed to connect to Postgres Database due to: {e}")
        raise
    return connection   


def insert_data(connection, dataset):
    try:
        connection.rollback()
        cursor = connection.cursor()
        insert_query = """
        INSERT INTO clickstream.users (
            id, first_name, last_name, gender, street_address,city,state,country, postal_code, email, username, 
            date_of_birth, registered_date, phone, picture
        ) VALUES %s
        """
        execute_values(cursor, insert_query, dataset)
        connection.commit()

    except Exception as e:
        logging.error("Error inserting data into users table: {e}")
        raise

def users_init():
    data = get_raw_data(random_user_endpoint)
    ids, data = transform_raw_data(data)
    connection = db_connect(postgres_db_config)
    insert_data(connection, data)
    connection.close()
    return ids



if __name__ == "__main__":
    users_init()