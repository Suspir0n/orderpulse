from pytest import raises
from app.core.entities.user_entities import User


def test_entitie_user_providing_missing_data():
    username = 'test'
    first_name = 'test'
    last_name = 'testing'
    email = 'test@testing.com'

    with raises(TypeError) as excinfo:
        User(username, first_name, last_name, email)

    assert "missing 1 required" in str(excinfo.value)
