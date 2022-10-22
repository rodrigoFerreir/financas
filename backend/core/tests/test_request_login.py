import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


class TestAuthentication:
    def test_initial_login_status_code(self):
        res = client.post(
            "/api/auth/login",
            json={"email": "rodrigo.s@teste.com", "password": "123456"},
        )
        assert res.status_code == 200

    def test_initial_login_message_err(self):
        res = client.post(
            "/api/auth/login",
            json={"email": "rodrigo.s@teste.com", "password": "12345"},
        )
        assert res.json() == {"detail": "Erro interno no servidor"}

    def test_initial_login_message_bad_request(self):
        res = client.post(
            "/api/auth/login",
            json={"email": "rodrigo.s@teste.co", "password": "123456"},
        )
        assert res.status_code == 500

    def test_initial_login_body_request_err(self):
        res = client.post(
            "/api/auth/login",
            json={"emai": "rodrigo.s@teste.com", "password": "123456"},
        )
        assert res.status_code != 200

    def test_initial_login_return_request_err(self):
        res = client.post(
            "/api/auth/login",
            json={"emai": "rodrigo.s@teste.com", "password": "123456"},
        )
        assert res.json() != {}

    def test_initial_login_return_request_token(self):
        res = client.post(
            "/api/auth/login",
            json={"email": "rodrigo.s@teste.com", "password": "123456"},
        )
        if res.status_code == 200:
            assert "token" in res.json()
