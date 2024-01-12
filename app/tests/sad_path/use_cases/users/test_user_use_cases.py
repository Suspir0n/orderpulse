from pytest import raises
from app.tests.fixtures.invalid_users_fixtures import INVALID_FIELD_TO_USER_USE_CASE


def test_create_user_one_invalid_field_or_missing_required(user_use_cases):
    with raises(TypeError) as excinfo:
        user_use_cases.execute(INVALID_FIELD_TO_USER_USE_CASE)

    assert "required positional arguments" in str(excinfo.value)