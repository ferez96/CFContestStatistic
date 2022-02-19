from pymongo import MongoClient
import pytest


@pytest.fixture()
def dbname():
    import config
    CONNECTION_STRING = f"{config.MONGODB_DRIVER}://{config.MONGODB_USERNAME}:{config.MONGODB_PASSWORD}@{config.MONGODB_HOST}/test"

    client = MongoClient(CONNECTION_STRING)
    yield client['test']
    # teardown

    client.close()


@pytest.fixture()
def collection_name(dbname):
    yield dbname['test_client']
    # teardown
    dbname.drop_collection('test_client')


def test_interaction_with_db(collection_name):
    item_1 = {
        "_id": "U1IT00001",
        "item_name": "Blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340,
        "category": "kitchen appliance"
    }

    item_2 = {
        "_id": "U1IT00002",
        "item_name": "Egg",
        "category": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs"
    }
    collection_name.insert_many([item_1, item_2])

    item_details = list(collection_name.find())
    assert len(item_details) == 2
    assert item_details[0] == {
        "_id": "U1IT00001",
        "item_name": "Blender",
        "max_discount": "10%",
        "batch_number": "RR450020FRG",
        "price": 340,
        "category": "kitchen appliance"
    }
    assert item_details[1] == {
        "_id": "U1IT00002",
        "item_name": "Egg",
        "category": "food",
        "quantity": 12,
        "price": 36,
        "item_description": "brown country eggs"
    }
