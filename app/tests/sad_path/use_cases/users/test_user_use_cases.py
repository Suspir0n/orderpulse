from pytest import raises
from app.tests.fixtures.invalid_users_fixtures import INVALID_FIELD_TO_USER_USE_CASE
from app.tests.fixtures.valid_users_fixtures import USER_DATA_TO_USE_CASE


def test_create_user_one_invalid_field_or_missing_required(create_user_use_case):
    with raises(TypeError) as excinfo:
        create_user_use_case.execute(INVALID_FIELD_TO_USER_USE_CASE)

    assert "required positional arguments" in str(excinfo.value)


def test_get_by_id_user_one_with_id_invalid(get_by_user_use_case, create_user_use_case):
    user_id = create_user_use_case.execute(**USER_DATA_TO_USE_CASE).inserted_id
    user_data = get_by_user_use_case.execute(user_id=user_id)

    assert user_id is not None
    assert user_id == user_data['_id']
    assert user_data['username'] == USER_DATA_TO_USE_CASE['username']