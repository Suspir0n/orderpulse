from app.tests.fixtures.valid_users_fixtures import USER_DATA

def test_create_user_one(user_repository):
    user_id = user_repository.create_user(USER_DATA).inserted_id

    assert user_id is not None
    assert user_id == USER_DATA['_id']

def test_get_by_id_user(user_repository):
    user_id = user_repository.create_user(USER_DATA).inserted_id

    result = user_repository.get_user_by_id(user_id=USER_DATA['_id'])

    assert user_id is not None
    assert user_id == USER_DATA['_id']
    assert result['_id'] == USER_DATA['_id']

def test_get_all_user(user_repository):
    user_id = user_repository.create_user(USER_DATA).inserted_id

    result = user_repository.get_all_users()

    assert user_id is not None
    assert user_id == USER_DATA['_id']
    assert len(result) == 1

def test_update_user(user_repository):
    user_id = user_repository.create_user(USER_DATA).inserted_id

    updated_data = {
        'username': 'test_user_updating',
        'first_name': 'test',
        'last_name': 'testing',
        'email': 'test@example.com',
        'password': 'test'
    }

    result_updating = user_repository.update_user(USER_DATA['_id'], updated_data)
    result_get_one = user_repository.get_user_by_id(user_id=USER_DATA['_id'])

    assert user_id is not None
    assert user_id == USER_DATA['_id']
    assert result_updating.modified_count == 1
    assert result_get_one is not None
    assert result_get_one['username'] == updated_data['username']

def test_delete_user(user_repository):
    user_id = user_repository.create_user(USER_DATA).inserted_id
    delete_user_result = user_repository.delete_user(user_id=USER_DATA['_id'])
    has_user_with_id = user_repository.get_user_by_id(user_id=USER_DATA['_id'])

    assert user_id is not None
    assert user_id == USER_DATA['_id']
    assert delete_user_result.deleted_count == 1
    assert has_user_with_id is None



