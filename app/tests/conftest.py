import pytest
import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.app import app
from app.core.repositories.user_repository import UserRepository
from app.core.adpters.mongo_adapter import MongoAdapter

load_dotenv()

APP_URL = os.getenv('APP_URL')
MONGO_URL = os.getenv('MONGO_URL')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')


@pytest.fixture
def app_client():
    client = TestClient(app)
    return client, APP_URL

@pytest.fixture(scope='module')
def user_repository():
    return UserRepository()

@pytest.fixture(scope='module')
def mongo_adapter():
    adapter = MongoAdapter()
    yield adapter
    adapter.close_connection()

@pytest.fixture(autouse=True)
def clean_database(user_repository):
    user_repository.collection.delete_many({})