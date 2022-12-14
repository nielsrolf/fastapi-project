import datetime as dt

from fastapi.testclient import TestClient
from jose import jwt

from {{cookiecutter.repo_name}}.authentication import ALGORITHM, JWT_SECRET
from {{cookiecutter.repo_name}}.main import app

client = TestClient(app)


def generate_test_token() -> str:
    """For debugging only: generate a token for a given username"""
    to_encode = {
        "sub": "testuser",
        "exp": dt.datetime.utcnow() + dt.timedelta(minutes=30),
    }
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt
