import pytest
from pymongo import MongoClient
from mongomock import MongoClient as MockMongoClient

@pytest.fixture(scope='session')
def mongo_database():
    # Use um banco de dados real para testes de integração ou um banco de dados mock para testes unitários
    client = MongoClient('mongodb://localhost:27017')  # Altere a conexão para seu MongoDB real
    db = client['test_database']  # Altere o nome do banco de dados conforme necessário
    yield db
    client.drop_database('test_database')  # Limpe o banco de dados após os testes

