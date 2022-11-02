from sensor.configuration.mango_db_connection import MongoDBClient
from sensor.exception import SensorException


def test_exception():
    try:
        

if __name__ == '__main__':
    mongodb_client = MongoDBClient()
    print("collection name",mongodb_client.database.list_collection_names())