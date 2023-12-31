import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from app.app import app

load_dotenv()

env_app_url = os.getenv("APP_URL")
client = TestClient(app)