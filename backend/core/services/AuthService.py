from time import time
from decouple import config

import jwt
from serializers.UserSerializer import UserLogin
from repositories.UserRepository import UserRepository
from utils.AuthUtil import verify_hash_password

JWT_SECRET = config("JWT_SECRET")


class AuthService:
    def create_jwt_token(self, user_id: str) -> str:
        payload = {
            "user_id": user_id,
            "expires": time() + 60 * 60,
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")

        return token

    def decode_jwt_token(self, token: str):
        try:
            decode_token = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])

            if decode_token["expires"] >= time():
                return decode_token
            else:
                return None

        except Exception as error:
            return {"msg": "Erro interno no servidor", "dados": "", "status": 500}

    async def login_service(self, user: UserLogin):
        try:
            user_repository = UserRepository()
            user_listed = await user_repository.list_user_from_email(email=user.email)

            if user_listed != None:
                if verify_hash_password(user.password, user_listed["password"]):
                    return {
                        "msg": "Login realizado com sucesso!",
                        "dados": user_listed,
                        "status": 200,
                    }
                else:
                    return {
                        "msg": "Email ou Senha incorretos",
                        "dados": "",
                        "status": 401,
                    }
            else:
                return {
                    "msg": "Email ou Senha incorretos",
                    "dados": "",
                    "status": 401,
                }
        except Exception as err:
            return {"msg": "Erro interno no servidor", "dados": "", "status": 500}
