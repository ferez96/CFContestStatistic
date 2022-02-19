from pymongo import MongoClient
import pytest


@pytest.fixture()
def mongo_testdb():
    import config
    CONNECTION_STRING = f"{config.MONGODB_DRIVER}://{config.MONGODB_USERNAME}:{config.MONGODB_PASSWORD}@{config.MONGODB_HOST}/test"

    client = MongoClient(CONNECTION_STRING)
    yield client['test']
    # teardown

    client.close()
