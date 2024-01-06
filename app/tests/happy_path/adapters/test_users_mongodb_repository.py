from app.core.adpters.users_mongo_repository import MongoRepository
from app.tests.fixtures.valid_users_fixtures import USER_DATA, USERS_DATA

def test_create_user_one(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    created_user_result = repository.create_user_one(USER_DATA)

    assert created_user_result.inserted_id is not None
    assert created_user_result.inserted_id == USER_DATA['_id']

def test_get_by_uuid_user(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    created_user_result = repository.create_user_one(USER_DATA)

    result = repository.get_user_by_id(_id=USER_DATA['_id'])

    assert created_user_result.inserted_id is not None
    assert created_user_result.inserted_id == USER_DATA['_id']
    assert result['_id'] == USER_DATA['_id']

def test_get_all_user(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    created_users_result = repository.create_user_many(USERS_DATA)

    result = repository.get_all_user()

    assert created_users_result.inserted_ids is not None
    assert created_users_result.inserted_ids[0] == USERS_DATA[0]['_id']
    assert created_users_result.inserted_ids[1] == USERS_DATA[1]['_id']
    assert created_users_result.inserted_ids[2] == USERS_DATA[2]['_id']
    assert result.explain()['executionStats']['executionStages']['numReads'] == 3

def test_update_user(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    created_users_result = repository.create_user_many(USERS_DATA)

    _user_data = {
        'username': 'test_user_updating',
        'first_name': 'test',
        'last_name': 'testing',
        'email': 'test@example.com',
        'password': 'test'
    }

    result_updating = repository.get_update_user(USERS_DATA[1]['_id'], _user_data)
    result_get_one = repository.get_user_by_id(_id=USERS_DATA[1]['_id'])

    assert created_users_result.inserted_ids is not None
    assert created_users_result.inserted_ids[0] == USERS_DATA[0]['_id']
    assert created_users_result.inserted_ids[1] == USERS_DATA[1]['_id']
    assert created_users_result.inserted_ids[2] == USERS_DATA[2]['_id']
    assert result_updating.modified_count == 1
    assert result_get_one is not None
    assert result_get_one['username'] == _user_data['username']



