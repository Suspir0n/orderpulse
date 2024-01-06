from app.core.adpters.users_mongo_repository import MongoRepository
from pytest import raises
from app.tests.fixtures.invalid_users_fixtures import INVALID_FIELD_OR_MISSING_REQUIRED_USER_DATA, \
    INVALID_TYPE_FIELD_USER_DATA, INVALID_DUPLICATE_USER_DATA, INVALID_OBJECT_ID_USER_DATA


def test_create_user_one_invalid_field_or_missing_required(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    with raises(ValueError) as excinfo:
        repository.create_user_one(INVALID_FIELD_OR_MISSING_REQUIRED_USER_DATA)

    assert "missing from the user data." in str(excinfo.value)


def test_create_user_one_invalid_type_field(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    with raises(TypeError) as excinfo:
        repository.create_user_one(INVALID_TYPE_FIELD_USER_DATA)

    assert "All fields must be strings." in str(excinfo.value)

def test_create_user_one_duplicated(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    with raises(ValueError) as excinfo:
        repository.create_user_one(INVALID_DUPLICATE_USER_DATA)
        repository.create_user_one(INVALID_DUPLICATE_USER_DATA)

    assert "There is already a user with this email." in str(excinfo.value)

def test_get_by_id_invalid_object_id(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    with raises(ValueError) as excinfo:
        repository.get_user_by_id(INVALID_OBJECT_ID_USER_DATA)

    assert "Invalid user ID." in str(excinfo.value)



