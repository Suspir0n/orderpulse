from app.tests.fixtures.valid_users_fixtures import USER_DATA_TO_USE_CASE

def test_create_user_one(create_user_use_case):
    user_id = create_user_use_case.execute(**USER_DATA_TO_USE_CASE).inserted_id

    assert user_id is not None

def test_get_by_id_user_one_with_id_invalid(get_by_user_use_case, create_user_use_case):
    user_id = create_user_use_case.execute(**USER_DATA_TO_USE_CASE).inserted_id
    user_data = get_by_user_use_case.execute(user_id=user_id)

    assert user_id is not None
    assert user_id == user_data['_id']
    assert user_data['username'] == USER_DATA_TO_USE_CASE['username']

def test_get_all_users(get_all_users_use_case, create_user_use_case):
    user_id = create_user_use_case.execute(**USER_DATA_TO_USE_CASE).inserted_id
    user_data = get_all_users_use_case.execute()

    assert user_id is not None
    assert len(user_data) == 1