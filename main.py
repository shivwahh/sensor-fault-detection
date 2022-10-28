from sensor.configuration.mango_db_connection import MangoDBClient


if __name__ == '__main__':
    mongodb_client = MangoDBClient()
    print("collection name",mongodb_client.database.list_collection_names())