import pytest
import requests
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


class TestRequestUsers:
    pass
