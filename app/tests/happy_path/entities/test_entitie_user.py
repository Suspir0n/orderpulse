from pytest import raises
from app.core.entities.user_entities import User


def test_entitie_user_providing_all_valid_data():
    uuid = 'abc123'
    username = 'test'
    first_name = 'test'
    last_name = 'testing'
    email = 'test@testing.com'
    password = '1234'

    user = User(uuid, username, first_name, last_name, email, password)

    assert user.uuid == uuid
    assert user.username == username
    assert user.first_name == first_name
    assert user.last_name == last_name
    assert user.email == email
    assert user.password == password


