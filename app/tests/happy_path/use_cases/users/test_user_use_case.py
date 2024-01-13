from pytest import raises
from app.tests.fixtures.valid_users_fixtures import USER_DATA_TO_USE_CASE

def test_create_user_one(create_user_use_case):
    user_id = create_user_use_case.execute(**USER_DATA_TO_USE_CASE).inserted_id

    assert user_id is not None

def test_get_by_id_user_one(get_by_user_use_case, create_user_use_case):
    user_id_invalind = '123'

    with raises(ValueError) as excinfo:
        get_by_user_use_case.execute(user_id=user_id_invalind)

    assert "Invalid user ID." in str(excinfo.value)