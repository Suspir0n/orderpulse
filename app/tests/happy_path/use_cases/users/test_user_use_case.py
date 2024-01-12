from app.tests.fixtures.valid_users_fixtures import USER_DATA_TO_USE_CASE

def test_create_user_one(user_use_cases):
    user_id = user_use_cases.execute(**USER_DATA_TO_USE_CASE).inserted_id

    assert user_id is not None