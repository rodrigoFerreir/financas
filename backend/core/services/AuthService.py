
from time import time
from decouple import config

import jwt
from serializers.UserSerializer import UserLogin
from repositories.UserRepository import list_user_from_email
from utils.AuthUtil import (verify_hash_password)

JWT_SECRET = config('JWT_SECRET')


def create_jwt_token(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "expires": time() + 600,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm='HS256')

    return token


def decode_jwt_token(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])

        if decode_token["expires"] >= time():
            return decode_token
        else:
            return None

    except Exception as error:
        print(error)
        return {
            "msg": "Erro interno no servidor",
            "dados": "",
            "status": 500
        }


async def login_service(user: UserLogin):
    user_listed = await list_user_from_email(user.email)

    if user_listed:
        if verify_hash_password(user.password, user_listed["password"]):
            return {
                "msg": "Login realizado com sucesso!",
                "dados": user_listed,
                "status": 200
            }
        else:
            return {
                "msg": "Email ou Senha incorretos",
                "dados": "",
                "status": 401
            }

    else:
        return {
            "msg": "Email ou Senha incorretos",
            "dados": "",
            "status": 401
        }
