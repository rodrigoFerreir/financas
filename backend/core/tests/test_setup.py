import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


class TestSetup:
    def test_from_initial_setup(self):
        res = client.get("/api/health")
        assert res.json() == {"status": "ok"}
