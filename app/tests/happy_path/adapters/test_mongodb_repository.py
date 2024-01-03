from bson.objectid import ObjectId
import pytest
from pymongo import MongoClient
from app.core.adpters.mongo_repository import MongoDBRepository

# Mock de um documento para testes
TEST_DOCUMENT = {
        "uuid": ObjectId("61774b56c7091e830d495120"),
        'username': 'test',
        'first_name': 'test',
        'last_name': 'testing',
        'email': 'test@testing.com',
        'password': '1234'
    }

# Fixture para o MongoDBRepository com a coleção temporária para testes
@pytest.fixture
def mongo_repo(mongo_database):
    test_db = mongo_database["test_database"]
    test_collection = test_db["test_collection"]
    test_collection.insert_one(TEST_DOCUMENT)
    yield MongoDBRepository(mongo_database, "test_database", "test_collection")
    test_collection.drop()

# Teste de leitura (read)
def test_read_document(mongo_repo):
    query = {"username": "test"}
    result = mongo_repo.read(query)
    assert result == TEST_DOCUMENT

# Teste de criação (create)
def test_create_document(mongo_repo, mongo_database):
    data = {
        'username': 'test',
        'first_name': 'test',
        'last_name': 'testing',
        'email': 'test@testing.com',
        'password': '1234'
    }
    inserted_id = mongo_repo.create(data)
    assert isinstance(inserted_id, str)

    # Verifica se o documento foi inserido corretamente no banco de dados
    inserted_document = mongo_database["test_database"]["test_collection"].find_one({"uuid": ObjectId(inserted_id)})
    assert inserted_document["username"] == "test"
    assert inserted_document["email"] == 'test@testing.com'

# Teste de atualização (update)
def test_update_document(mongo_repo, mongo_database):
    query = {"username": "test"}
    new_data = {"$set": {"email": 'test01@testing.com'}}
    updated = mongo_repo.update(query, new_data)
    assert updated

    # Verifica se o documento foi atualizado corretamente no banco de dados
    updated_document = mongo_database["test_database"]["test_collection"].find_one({"username": "test"})
    assert updated_document["email"] == 'test01@testing.com'

# Teste de exclusão (delete)
def test_delete_document(mongo_repo):
    query = {"username": "test"}
    deleted = mongo_repo.delete(query)
    assert deleted

    # Verifica se o documento foi deletado corretamente do banco de dados
    assert mongo_repo.read(query) is None