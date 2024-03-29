import pytest


@pytest.fixture()
def mongodb_with_members(mongo_testdb):
    mongo_testdb["members"].insert_many(
        [
            {
                "_id": 1,
                "name": "Duong Thai Minh",
                "codeforces_handle": "I_UsedTo_Love_You",
                "codeforces": {
                    "handle": "I_UsedTo_Love_You",
                    "rating": 1500,
                },
            },
            {
                "_id": 2,
                "name": "Truong Cong Thanh",
                "codeforces_handle": "TYT",
                "codeforces": None,
            }
        ]
    )
    yield mongo_testdb

    # teardown
    mongo_testdb.drop_collection("members")
