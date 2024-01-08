from app.core.repositories.user_repository import UserRepository
from app.tests.fixtures.valid_users_fixtures import USER_DATA, USERS_DATA

def test_create_user_one(mongo_client):
    repository = UserRepository()

    created_user_result = repository.create_user(USER_DATA)

    assert created_user_result.inserted_id is not None
    assert created_user_result.inserted_id == USER_DATA['_id']

def test_get_by_id_user(mongo_client):
    repository = UserRepository()

    created_user_result = repository.create_user(USER_DATA)

    result = repository.get_user_by_id(user_id=USER_DATA['_id'])

    assert created_user_result.inserted_id is not None
    assert created_user_result.inserted_id == USER_DATA['_id']
    assert result['_id'] == USER_DATA['_id']

def test_get_all_user(mongo_client):
    repository = UserRepository()

    created_users_result = repository.create_user(USER_DATA)

    result = repository.get_all_users()

    assert created_users_result.inserted_ids is not None
    assert created_users_result.inserted_ids == USER_DATA['_id']
    assert result.explain()['executionStats']['executionStages']['numReads'] == 1

def test_update_user(mongo_client):
    repository = UserRepository()

    created_users_result = repository.create_user(USER_DATA)

    _user_data = {
        'username': 'test_user_updating',
        'first_name': 'test',
        'last_name': 'testing',
        'email': 'test@example.com',
        'password': 'test'
    }

    result_updating = repository.update_user(USER_DATA['_id'], _user_data)
    result_get_one = repository.get_user_by_id(user_id=USERS_DATA['_id'])

    assert created_users_result.inserted_ids is not None
    assert created_users_result.inserted_ids == USERS_DATA['_id']
    assert result_updating.modified_count == 1
    assert result_get_one is not None
    assert result_get_one['username'] == _user_data['username']

def test_delete_user(mongo_client):
    repository = UserRepository()

    created_user_result = repository.create_user(USER_DATA)
    delete_user_result = repository.delete_user(user_id=USER_DATA['_id'])
    has_user_with_id = repository.get_user_by_id(user_id=USER_DATA['_id'])

    assert created_user_result.inserted_id is not None
    assert created_user_result.inserted_id == USER_DATA['_id']
    assert delete_user_result.deleted_count == 1
    assert has_user_with_id is None



