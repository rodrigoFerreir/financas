from fastapi import Header, HTTPException
from services.AuthService import AuthService


class AuthMiddleware:
    auth_service = AuthService()

    async def verify_token(self, Authorization: str = Header(default="")):
        if not Authorization.split(" ")[0] == "Bearer":
            raise HTTPException(status_code=401, detail="Token invalido")

        token = Authorization.split(" ")[1]

        payload = self.auth_service.decode_jwt_token(token)

        if not payload:
            raise HTTPException(status_code=401, detail="Token invalido ou expirado")

        return payload
