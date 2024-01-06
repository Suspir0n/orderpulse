from app.core.adpters.mongo_repository import MongoRepository
from bson.objectid import ObjectId

TEST_DOCUMENT = {
    "uuid": ObjectId("61774b56c7091e830d495120"),
    'username': 'test_user',
    'first_name': 'test',
    'last_name': 'testing',
    'email': 'test@example.com',
    'password': 'password123'
}

TEST_DOCUMENT_TWO = {
    "uuid": ObjectId("61774b56c7091e830d495380"),
    'username': 'test_user',
    'first_name': 'test',
    'last_name': 'testing',
    'email': 'test@example.com',
    'password': 'password123'
}

def test_create_user(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    repository.create_user(TEST_DOCUMENT)

    assert mongo_client.test_db.users.find_one({'uuid': ObjectId("61774b56c7091e830d495120")}) is not None


def test_get_by_uuid_user(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    repository.create_user(TEST_DOCUMENT)

    response = repository.get_user_by_id(user_id=ObjectId("61774b56c7091e830d495120"))

    assert response['uuid'] == ObjectId("61774b56c7091e830d495120")

def test_get_all_user(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    repository.create_user(TEST_DOCUMENT)
    repository.create_user(TEST_DOCUMENT_TWO)

    response = repository.get_all_user()

    assert response.explain()['executionStats']['executionStages']['numReads'] == 2

def test_update_user(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    repository.create_user(TEST_DOCUMENT)

    _TEST_DOCUMENT = {
        "uuid": ObjectId("61774b56c7091e830d495380"),
        'username': 'test_user_updating',
        'first_name': 'test_Ola',
        'last_name': 'testing',
        'email': 'test@example.com',
        'password': 'password123'
    }

    response = repository.get_update_user(TEST_DOCUMENT, _TEST_DOCUMENT)

    assert response.modified_count == 1



