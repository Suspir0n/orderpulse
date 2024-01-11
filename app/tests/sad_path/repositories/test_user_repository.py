from pytest import raises
from app.tests.fixtures.valid_users_fixtures import USER_DATA
from app.tests.fixtures.invalid_users_fixtures import INVALID_FIELD_OR_MISSING_REQUIRED_USER_DATA, \
    INVALID_TYPE_FIELD_USER_DATA, INVALID_DUPLICATE_USER_DATA, INVALID_OBJECT_ID_USER_DATA, INVALID_USER_DATA_NO_EXISTS


def test_create_user_one_invalid_field_or_missing_required(user_repository):
    with raises(ValueError) as excinfo:
        user_repository.create_user(INVALID_FIELD_OR_MISSING_REQUIRED_USER_DATA)

    assert "missing from the user data." in str(excinfo.value)


def test_create_user_one_invalid_type_field(user_repository):
    with raises(TypeError) as excinfo:
        user_repository.create_user(INVALID_TYPE_FIELD_USER_DATA)

    assert "All fields must be strings." in str(excinfo.value)

def test_create_user_one_duplicated(user_repository):
    with raises(ValueError) as excinfo:
        user_repository.create_user(INVALID_DUPLICATE_USER_DATA)
        user_repository.create_user(INVALID_DUPLICATE_USER_DATA)

    assert "There is already a user with this email." in str(excinfo.value)

def test_get_by_id_invalid_object_id(user_repository):
    with raises(ValueError) as excinfo:
        user_repository.get_user_by_id(INVALID_OBJECT_ID_USER_DATA)

    assert "Invalid user ID." in str(excinfo.value)

def test_update_user_invalid_object_id(user_repository):
    user_repository.create_user(USER_DATA)

    with raises(ValueError) as excinfo:
        user_repository.update_user(INVALID_OBJECT_ID_USER_DATA['_id'], INVALID_OBJECT_ID_USER_DATA)

    assert "Invalid user ID." in str(excinfo.value)

def test_update_user_invalid_type_field(user_repository):
    user_repository.create_user(USER_DATA)

    with raises(TypeError) as excinfo:
        user_repository.update_user(INVALID_TYPE_FIELD_USER_DATA['_id'], INVALID_TYPE_FIELD_USER_DATA)

    assert "All fields must be strings." in str(excinfo.value)

def test_delete_user_invalid_object_id(user_repository):
    with raises(ValueError) as excinfo:
        user_repository.delete_user(INVALID_OBJECT_ID_USER_DATA)

    assert "Invalid user ID." in str(excinfo.value)