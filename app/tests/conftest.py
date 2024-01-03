from pymongo import MongoClient
import pytest
import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.app import app

load_dotenv()

APP_URL = os.getenv('APP_URL')
MONGO_URL = os.getenv('MONGO_URL')
MONGO_USERNAME = os.getenv('MONGO_USERNAME')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')


@pytest.fixture
def app_client():
    client = TestClient(app)
    return client, APP_URL

@pytest.fixture
def mongo_client():
    client = MongoClient(
        MONGO_URL,
        username=MONGO_USERNAME,
        password=MONGO_PASSWORD
    )
    yield client
    client.drop_database('test_db')
