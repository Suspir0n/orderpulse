from app.core.adpters.mongo_repository import MongoRepository


def test_create_user(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    user_data = {
        'uuid': 'abc123',
        'username': 'test_user',
        'first_name': 'test',
        'last_name': 'testing',
        'email': 'test@example.com',
        'password': 'password123'
    }

    repository.create_user(user_data)

    assert mongo_client.test_db.users.find_one({'uuid': 'abc123'}) is not None


def test_get_by_uuid_user(mongo_client):
    repository = MongoRepository(mongo_client.test_db)

    user_data = {
        'uuid': 'abc123',
        'username': 'test_user',
        'first_name': 'test',
        'last_name': 'testing',
        'email': 'test@example.com',
        'password': 'password123'
    }

    repository.create_user(user_data)

    response = repository.get_user_by_id(user_id='abc123')

    assert response['uuid'] == 'abc123'